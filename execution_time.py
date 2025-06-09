import time
start_time = time.perf_counter()
for i in range(9999999):
    pass
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"The time elapsed for the program execution is: {elapsed_time:.2f} seconds")