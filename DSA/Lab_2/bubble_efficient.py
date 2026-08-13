def bub_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for n in range(i):
            if arr[n] > arr [n+1]:
                arr[n],arr[n+1] = arr[n+1],arr[n]
    return arr
a = [2,6,4,3,7,13,22,11,24,42]
print(bub_sort(a))
