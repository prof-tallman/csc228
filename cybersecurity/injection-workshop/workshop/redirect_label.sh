#!/bin/sh
# Workshop-only helper. It changes only a generated label inside this container.
order_id="$1"
case "$order_id" in
  ''|*[!0-9]*) echo "Usage: redirect_label.sh ORDER_ID" >&2; exit 2 ;;
esac
file="/app/data/labels/${order_id}.txt"
if [ ! -f "$file" ]; then
  echo "No workshop label exists for order ${order_id}." >&2
  exit 1
fi
python - "$file" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
text = p.read_text()
lines = text.splitlines()
try:
    i = lines.index("SHIP TO:")
    # Preserve customer name, replace next two address lines.
    lines[i+2:i+4] = ["500 Attacker Avenue", "Testville, CA 90000"]
except (ValueError, IndexError):
    raise SystemExit("Label format not recognized")
p.write_text("\n".join(lines) + "\n")
PY
printf "Workshop label %s redirected.\n" "$order_id"
