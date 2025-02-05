import time

start = time.time()

sum(range(1, 1000001))

end = time.time()

elapsed = end - start
print(f"Execution Time: {elapsed:.3f} seconds")