import time
import multiprocessing

def add():
    global x
    for i in range(10000000):
        x += 1
    

def subtract():
    global x
    for i in range(10000000):
        x -= 1

if __name__ == "__main__":
    x = 0
    start = time.perf_counter()
    p1 = multiprocessing.Process(target = subtract)
    # 1. Add 1 line of Python to launch a new process which executes the add function
    end = time.perf_counter()
    print('final x =' + str(x))
    print(f'elapsed time = {end - start}')
    
# 2. What value of X does approaching this problem with multiprocessing result in?

# 3. Why do you think X behaves this way?
