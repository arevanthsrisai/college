def search(a, i):
    global n
    n += 1
    if len(a) == 0:
        return "notfound"
    elif a[1] == i:
        return f"found at index {n}"
    return search(a[1:len(a)],i)
n=0
a = [2,4,5,1,9,7,3]
print(search(a,1))
