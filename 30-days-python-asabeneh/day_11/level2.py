import multiprocessing as mp

def func1(num):
    p = 1
    for i in range(1, num + 1):
        p *= i
    return p

def compute_chunk(start, end, deg):
    s = 0
    for i in range(start, end, 4):
        s += (deg ** i) / func1(i)
    for j in range(start + 2, end, 4):
        s -= (deg ** j) / func1(j)
    return s

def funcnew(deg):
    num_processes = mp.cpu_count()
    chunk_size = 10000 // num_processes
    pool = mp.Pool(processes=num_processes)
    
    results = [pool.apply_async(compute_chunk, args=(i, i + chunk_size, deg)) for i in range(0, 100000, chunk_size)]
    pool.close()
    pool.join()
    
    return 1 + sum(result.get() for result in results)

if __name__ == "__main__":
    print(funcnew(45))

    # Output:
    #1056.2538455391366