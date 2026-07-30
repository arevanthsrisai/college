def search(a, i, n):
    if n > len(a):
        return "not found"
    elif len(a) == 0:
        return "empty list"
    elif n < len(a) and a[n] == i:
        return f"found at index {n}"
    
    return search(a,i,n+1)
a = [2,4,5,1,9,7,3]
print(search(a,1,0))

#a is list, i is id, n is search from index.
