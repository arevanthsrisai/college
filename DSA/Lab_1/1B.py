def calc(p,n):
    if n == 0:
        return 1
    return p*calc(p,n-1)

print(calc(2,-1))
