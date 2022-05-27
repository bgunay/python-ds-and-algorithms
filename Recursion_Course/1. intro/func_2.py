def func(n):
    if n == 1:
        print(1)
    else:
        func(n-1)
        print(n)
        func(n-1)


func(4)