#  Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
  time.sleep(2)
  return f"Square: {number * number}"

numbers=[1,2,3,4,5,6,7,8,9,11,2,3,12,14]
if __name__=="__main__":  # Without this, Windows may spawn infinite processes.

  with ProcessPoolExecutor(max_workers=3) as executor:
    results=executor.map(square_number,numbers)

  for result in results:
    print(result)


# ProcessPoolExecutor runs tasks in separate processes to achieve true parallelism.
# It is ideal for CPU-bound workloads because it bypasses the GIL.
# The GIL is a lock in CPython that allows only one thread to execute Python bytecode at a time.
