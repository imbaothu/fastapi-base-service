import threading
import time

counter = 0

def increment():
    global counter
    local_counter = counter
    local_counter += 1
    # assume time.sleep to increase raise race condition
    time.sleep(0.0001)
    counter = local_counter

threads = []
for _ in range(1000):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
# Final counter value: 323
# Final counter value: 334
