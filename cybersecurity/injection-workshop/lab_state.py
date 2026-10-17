from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "business.db"
VENDOR_PATH = DATA_DIR / "vendors.txt"
NOTES_PATH = DATA_DIR / "internal_notes.txt"
QUEUE_PATH = DATA_DIR / "shipping_queue.txt"
LABEL_DIR = DATA_DIR / "labels"

CUSTOMERS = [
    (1, "Acme Office Supply", "Maria Lopez", "maria@acme.example", "2450 Harbor Blvd.", "Costa Mesa", "CA", "92626"),
    (27523, "Blue Harbor Coffee", "Nina Patel", "nina@blueharbor.example", "88 Ocean View Rd.", "Dana Point", "CA", "92629"),
    (33923, "Mountain View Dental", "Dr. Susan Chen", "susan@mountainview.example", "1820 Main Street", "Irvine", "CA", "92614"),
    (47293, "Evergreen Accounting", "Tara Nguyen", "tara@evergreen.example", "740 Civic Center Dr.", "Santa Ana", "CA", "92701"),
    (52535, "Golden State Printworks", "Luis Romero", "luis@goldenstate.example", "9100 Industry Way", "Anaheim", "CA", "92806"),
    (67836, "Harborlight Landscaping", "Maya Chen", "maya@harborlight.example", "77 Garden Lane", "Laguna Hills", "CA", "92653"),
    (77439, "Juniper Market", "Avery Brooks", "avery@juniper.example", "151 Juniper Ave.", "Tustin", "CA", "92780"),
    (84873, "Pacific Crest Design", "Elena Garcia", "elena@pacificcrest.example", "320 Studio Court", "Newport Beach", "CA", "92660"),
]

ORDERS = [
    (1042, 1, "Printer paper — 12 cases", 428.00, "Open", "Packing"),
    (1057, 33923, "Toner cartridges — assorted", 612.00, "Open", "Awaiting shipment"),
    (1061, 33923, "Sterilization supplies", 865.00, "Open", "Packing"),
    (1074, 27523, "Coffee cup sleeves", 294.00, "Open", "Scheduled delivery"),
    (1080, 47293, "Archive boxes", 356.00, "Open", "Awaiting shipment"),
    (1088, 52535, "Wide-format paper", 721.00, "Open", "Packing"),
    (1091, 67836, "Irrigation fittings", 488.00, "Open", "Scheduled delivery"),
    (1103, 77439, "Receipt paper", 179.00, "Open", "Awaiting shipment"),
]

VENDORS = """Acme Freight | 800-555-0141 | Regional shipping\nBlue Line Packaging | 800-555-0188 | Boxes and packing supplies\nCanyon Office Products | 800-555-0127 | Office supplies\nNorthstar Logistics | 800-555-0195 | Preferred freight carrier\nPacific Print Services | 800-555-0133 | Commercial printing\nSummit IT Services | 800-555-0174 | Managed IT services\n"""

INTERNAL_NOTES = """INTERNAL PURCHASING NOTES\n\nPreferred freight vendor: Northstar Logistics\nWarehouse alarm inspection: October 15\nAccounting contact: Dana Reed\nBackup shipment process: Call warehouse manager directly\nQuarter-end inventory count: October 2\n"""


def _label_text(order_id, customer_id, item):
    customer = next(c for c in CUSTOMERS if c[0] == customer_id)
    return (
        f"EAGLES OUTDOOR SUPPLY — SHIPPING LABEL\n"
        f"Order #{order_id}\n\n"
        f"SHIP TO:\n{customer[1]}\n{customer[4]}\n{customer[5]}, {customer[6]} {customer[7]}\n\n"
        f"CONTENTS:\n{item}\n"
    )


def reset_lab():
    DATA_DIR.mkdir(exist_ok=True)
    LABEL_DIR.mkdir(exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DROP TABLE IF EXISTS orders")
        conn.execute("DROP TABLE IF EXISTS customers")
        conn.execute("""
            CREATE TABLE customers (
                id INTEGER PRIMARY KEY,
                company TEXT NOT NULL,
                contact TEXT NOT NULL,
                email TEXT NOT NULL,
                street TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                postal_code TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE orders (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                item TEXT NOT NULL,
                amount REAL NOT NULL,
                status TEXT NOT NULL,
                fulfillment_stage TEXT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(id)
            )
        """)
        conn.executemany(
            "INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?)", CUSTOMERS
        )
        conn.executemany(
            "INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)", ORDERS
        )
        conn.commit()

    VENDOR_PATH.write_text(VENDORS, encoding="utf-8")
    NOTES_PATH.write_text(INTERNAL_NOTES, encoding="utf-8")

    queue_lines = ["TODAY'S SHIPPING QUEUE", ""]
    for order in ORDERS[:4]:
        cust = next(c for c in CUSTOMERS if c[0] == order[1])
        queue_lines.append(f"Order {order[0]} — {cust[1]} — ${order[3]:,.2f}")
    QUEUE_PATH.write_text("\n".join(queue_lines) + "\n", encoding="utf-8")

    for path in LABEL_DIR.glob("*.txt"):
        path.unlink()
    for order in ORDERS:
        (LABEL_DIR / f"{order[0]}.txt").write_text(
            _label_text(order[0], order[1], order[2]), encoding="utf-8"
        )


if __name__ == "__main__":
    reset_lab()
    print(f"Reset workshop state in {DATA_DIR}")
