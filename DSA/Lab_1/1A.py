def launch(n):
    if n == 0:
        print("Launch!")
        return
    print(n)
    return launch(n-1)

n = int(input("enter number: "))
launch(n)
