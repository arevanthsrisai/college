def fib(n):
    if n <=2:
        return n-1
    return fib(n-1) + fib(n-2)
def fibo(n):
    if n > 0:
        fibo(n-1)
        print(fib(n))

n = int(input("enter n: "))

fibo(n)
