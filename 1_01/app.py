import time
import uuid
from datetime import datetime, timezone

# Generate a random UUID at the start
unique_id = uuid.uuid4()

# Infinite loop to output the UUID every 5 seconds
while True:
    current_time = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace("+00:00", "Z")
    print(f"{current_time}: {unique_id}")
    time.sleep(5)
