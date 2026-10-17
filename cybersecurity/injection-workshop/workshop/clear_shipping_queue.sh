#!/bin/sh
# Workshop-only helper. It changes only disposable data inside this container.
printf "TODAY'S SHIPPING QUEUE\n\n" > /app/data/shipping_queue.txt
printf "Workshop shipping queue cleared.\n"
