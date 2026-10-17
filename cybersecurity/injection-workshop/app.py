from flask import Flask, render_template, request, jsonify
import sqlite3
import subprocess
from pathlib import Path

from lab_state import (
    BASE_DIR, DB_PATH, VENDOR_PATH, NOTES_PATH, QUEUE_PATH, LABEL_DIR, reset_lab
)

app = Flask(__name__)
LOGGED_IN_CUSTOMER_ID = 1  # Acme Office Supply for the workshop story.


def query_db(sql, params=None):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(sql, params or [])
        return [dict(row) for row in cur.fetchall()]


def execute_db(sql, params=None):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(sql, params or [])
        conn.commit()
        return cur.rowcount


def debug(mode, user_input, statement, explanation, parameters=None):
    result = {
        "mode": mode,
        "input": user_input,
        "statement": statement,
        "explanation": explanation,
    }
    if parameters is not None:
        result["parameters"] = parameters
    return result


def customer_rows():
    return query_db("""
        SELECT id, company, contact, email,
               street || ', ' || city || ', ' || state || ' ' || postal_code AS address
        FROM customers ORDER BY id
    """)


def order_rows():
    return query_db("""
        SELECT o.id, o.customer_id, c.company, o.item, o.amount, o.status, o.fulfillment_stage
        FROM orders o JOIN customers c ON c.id = o.customer_id
        ORDER BY o.id
    """)


@app.route("/")
def index():
    cheatmode = request.args.get("cheatmode") == "1"
    return render_template("index.html", cheatmode=cheatmode)


@app.route("/api/state")
def state():
    customers = customer_rows()
    orders = order_rows()
    open_orders = [o for o in orders if o["status"] == "Open"]
    pending_revenue = sum(float(o["amount"]) for o in open_orders)
    return jsonify({
        "customers": customers,
        "orders": orders,
        "open_order_count": len(open_orders),
        "pending_revenue": pending_revenue,
        "shipping_queue": QUEUE_PATH.read_text(encoding="utf-8") if QUEUE_PATH.exists() else "",
    })


@app.route("/api/reset", methods=["POST"])
def reset():
    reset_lab()
    return jsonify({"ok": True, "message": "Workshop database and files restored."})


# ---------------------------- SQL INJECTION ----------------------------


@app.route("/api/sql/read", methods=["POST"])
def sql_read():
    body = request.get_json(force=True)
    term = body.get("term", "")
    secure = bool(body.get("secure", False))

    if not term:
        return jsonify({
            "rows": [],
            "error": "Please enter a search term.",
            "debug": None,
        })

    if secure:
        sql = """SELECT id, company, contact, email FROM customers
                 WHERE id = ? ORDER BY company"""
        params = [f"%{term}%"]
        rows = query_db(sql, params)
        return jsonify({
            "rows": rows,
            "debug": debug("secure", term, sql, "User input is bound separately as data.", params),
        })

    sql = f"SELECT id, contact, company, street, city, state, email FROM customers WHERE id = {term} ORDER BY company"
    try:
        rows = query_db(sql)
        error = None
    except sqlite3.Error as exc:
        rows, error = [], str(exc)
    return jsonify({
        "rows": rows,
        "error": error,
        "debug": debug("vulnerable", term, sql, "User input was inserted directly into the SQL statement."),
    })


@app.route("/api/sql/delete", methods=["POST"])
def sql_delete():
    body = request.get_json(force=True)
    order_id = str(body.get("order_id", ""))
    secure = bool(body.get("secure", False))

    if secure:
        sql = "DELETE FROM orders WHERE id = ? AND customer_id = ?"
        params = [order_id, LOGGED_IN_CUSTOMER_ID]
        try:
            count = execute_db(sql, params)
            error = None
        except sqlite3.Error as exc:
            count, error = 0, str(exc)
        return jsonify({
            "affected": count,
            "error": error,
            "debug": debug("secure", order_id, sql, "Order ID and customer ID are passed separately as data.", params),
        })

    sql = f"DELETE FROM orders WHERE id = {order_id} AND customer_id = {LOGGED_IN_CUSTOMER_ID}"
    try:
        count = execute_db(sql)
        error = None
    except sqlite3.Error as exc:
        count, error = 0, str(exc)
    return jsonify({
        "affected": count,
        "error": error,
        "debug": debug("vulnerable", order_id, sql, "The order ID was inserted directly into a DELETE statement."),
    })


@app.route("/api/sql/modify", methods=["POST"])
def sql_modify():
    body = request.get_json(force=True)
    field = body.get("field", "email")
    value = body.get("value", "")
    secure = bool(body.get("secure", False))
    allowed = {"contact", "email", "street"}
    if field not in allowed:
        return jsonify({"error": "Unsupported profile field."}), 400

    if secure:
        sql = f"UPDATE customers SET {field} = ? WHERE id = ?"
        params = [value, LOGGED_IN_CUSTOMER_ID]
        try:
            count = execute_db(sql, params)
            error = None
        except sqlite3.Error as exc:
            count, error = 0, str(exc)
        return jsonify({
            "affected": count,
            "error": error,
            "debug": debug("secure", value, sql, "The profile value is bound as data; the logged-in customer ID remains authoritative.", params),
        })

    sql = f"UPDATE customers SET {field} = '{value}' WHERE id = {LOGGED_IN_CUSTOMER_ID}"
    try:
        count = execute_db(sql)
        error = None
    except sqlite3.Error as exc:
        count, error = 0, str(exc)
    return jsonify({
        "affected": count,
        "error": error,
        "debug": debug("vulnerable", value, sql, "The profile value was inserted directly into an UPDATE statement."),
    })


@app.route("/api/password-reset", methods=["POST"])
def password_reset():
    body = request.get_json(force=True)
    customer_id = int(body.get("customer_id", 33923))
    rows = query_db("SELECT company, email FROM customers WHERE id = ?", [customer_id])
    if not rows:
        return jsonify({"error": "Account not found."}), 404
    row = rows[0]
    return jsonify({
        "company": row["company"],
        "destination": row["email"],
        "message": f"Password reset message sent to {row['email']}",
    })


# -------------------------- COMMAND INJECTION --------------------------


@app.route("/api/cmd/vendor", methods=["POST"])
def cmd_vendor():
    body = request.get_json(force=True)
    term = body.get("term", "")
    secure = bool(body.get("secure", False))

    if secure:
        command = ["grep", "-i", "--", term, str(VENDOR_PATH)]
        result = subprocess.run(command, capture_output=True, text=True)
        dbg = debug("secure", term, " ".join(command), "No shell is used; the user's text is one literal argument.", command)
    else:
        command = f'cat "{VENDOR_PATH}" | grep -i {term}'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        dbg = debug("vulnerable", term, command, "The user's input was inserted directly into a shell command.")

    output = result.stdout.strip()
    return jsonify({
        "output": output.splitlines() if output else [],
        "error": result.stderr.strip() or None,
        "debug": dbg,
    })


@app.route("/api/cmd/queue-search", methods=["POST"])
def cmd_queue_search():
    body = request.get_json(force=True)
    term = body.get("term", "")
    secure = bool(body.get("secure", False))
    if secure:
        command = ["grep", "-i", "--", term, str(QUEUE_PATH)]
        result = subprocess.run(command, capture_output=True, text=True)
        dbg = debug("secure", term, " ".join(command), "No shell is used; punctuation stays inside the search argument.", command)
    else:
        command = f'cat "{QUEUE_PATH}" | grep -i "{term}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        dbg = debug("vulnerable", term, command, "The queue search is constructed as a shell command, so injected commands can also execute.")
    output = result.stdout.strip()
    return jsonify({
        "output": output.splitlines() if output else [],
        "error": result.stderr.strip() or None,
        "debug": dbg,
    })


@app.route("/api/cmd/label", methods=["POST"])
def cmd_label():
    body = request.get_json(force=True)
    label_name = str(body.get("label_name", "1057"))
    secure = bool(body.get("secure", False))

    if secure:
        import re
        if not re.fullmatch(r"\d+", label_name):
            return jsonify({
                "label": "",
                "error": "Label number must look like 1057.",
                "debug": debug(
                    "secure",
                    label_name,
                    "read validated label",
                    "The application validates the label number and does not invoke a shell.",
                ),
            })
        path = LABEL_DIR / f"{label_name}.txt"
        label = path.read_text(encoding="utf-8") if path.exists() else "No label found."
        return jsonify({
            "label": label,
            "debug": debug("secure", label_name, f"read {path}", "The application reads the selected file directly; no command interpreter handles the input."),
        })
    else:
        command = f'cat "{LABEL_DIR}/{label_name}.txt"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({
            "label": result.stdout,
            "command_output": result.stdout.strip(),
            "error": result.stderr.strip() or None,
            "debug": debug(
                "vulnerable",
                label_name,
                command,
                "The label name was inserted directly into a shell command.",
            ),
})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
