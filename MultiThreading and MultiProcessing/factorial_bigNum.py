'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers,
involve significant computational work. Multiprocessing
can be used to distribute the workload across multiple
CPU cores, improving performance.

'''

import multiprocessing
import time
import sys
import math


# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

def compute_factorial(num):
  print(f"Computing factorial of {num}")
  result = math.factorial(num)
  print(f"Factorial of {num} is {result}")
  return result

if __name__ == '__main__':
   numbers = [6000,7000,7500,8000]

   start_time = time.time()

   # Create a pool of worker processes(Distributes tasks among worker)
   with multiprocessing.Pool() as pool:
      results = pool.map(compute_factorial, numbers)

   end_time = time.time()
   print(f"Results: {results}")
   print(f"Time taken: {end_time - start_time} seconds")
