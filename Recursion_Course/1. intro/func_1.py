def func(n):
    if n == 1:
        print(1)
    else:
        print(n)
        func(n-1)
        print(n)
        
func(5)