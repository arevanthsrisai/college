def bin_search(arr,e):
    l = 0
    h = len(arr)-1
    while l <= h:
        m = (l+h)//2
        if arr[m] == e:
            return m
        elif arr[m] > e:
            h = m-1
        else:
            l = m+1
    return -1
a = [2,6,4,3,7,13,22,11,24,42]
print(bin_search(a,13))
