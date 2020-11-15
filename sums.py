import functools
from time import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("**********Finished {} in {} secs".format(repr(func.__name__), round(run_time, 3)))
        return value

@timer
def sum_iterative(n):
    out=0
    for i in range(n+1):
        out += i
    return out

#recursive function calls itself until it reaches it's 'base case' or 'exit condition'
@timer
def sum_recursive(n):
    if n==1:
        return 1
    return n+sum_recursive(n-1)

@timer
def sum_optimal(n):
    return (n*(n+1))/2


if __name__ == "__main__":
    sum_iterative(10)