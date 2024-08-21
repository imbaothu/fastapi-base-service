import time
import multiprocessing
import threading

def cpu_bound_task(n):
    count = 0
    while count < 100000000:
        count += n

# Multiprocessing example
def multiprocessing_example():
    processes = []
    for _ in range(4):
        process = multiprocessing.Process(target=cpu_bound_task, args=(1,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

# Threading example
def threading_example():
    threads = []
    for _ in range(8):
        thread = threading.Thread(target=cpu_bound_task, args=(1,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start = time.time()
    multiprocessing_example()
    print("Multiprocessing time:", time.time() - start)
    
    start = time.time()
    threading_example()
    print("Threading time:", time.time() - start)
