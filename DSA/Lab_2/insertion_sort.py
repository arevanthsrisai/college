def ins_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

a = [2,6,4,3,7,13,22,11,24,42]
print(ins_sort(a))
       
                
