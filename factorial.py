# factorial funtcion is denoted with an exclamation point. is definied as product of integers from 1 to n

# n! = n*(n-1)*(n-2)
# 4! = 4*3*2*1

def fact(n):
    if n >= 0:
        if n == 0:
            return 1
        return n*fact(n-1)
    else:
        return "No negatives. Recursion error."
        
if __name__ == "__main__":
    print(fact(-3))