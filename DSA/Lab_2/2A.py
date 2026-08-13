def search(arr,e):
    for i in range(len(arr)):
        if arr[i] == e:
            return i
    return -1

a = [2,6,4,3,7,13,22,11,24,42]
print(search(a,12))
