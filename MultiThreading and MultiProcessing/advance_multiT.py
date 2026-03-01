# Multithreading With Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number :{number}"

numbers=[1,2,3,4,5,6,7,8,9,0,1,2,3]

with ThreadPoolExecutor(max_workers=3) as executor:
# At most 3 threads run simultaneously, other tasks wait in a queue, threads are reused (pooled)
    results=executor.map(print_number,numbers)
    # Submits all numbers to thread pool, executes function concurrently, returns results in same order as input

for result in results:
    print(result)


# Batch 1 → 3 tasks → 1 sec
# Batch 2 → 3 tasks → 1 sec
# Batch 3 → 3 tasks → 1 sec
# Batch 4 → 3 tasks → 1 sec
# Batch 5 → 1 task  → 1 sec

# Total ≈ 5 seconds
# Without threading → 13 seconds.

# ThreadPoolExecutor runs multiple tasks concurrently using a fixed number of worker threads.
# executor.map() applies a function to iterable items in parallel while preserving order.
