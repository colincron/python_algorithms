def fib(n):
    print(n)
    if n < 2: # base case
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    pass
#    fib(200)  

# write both recursive functions as loops and see which perform better