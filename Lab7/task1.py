def factor (n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*factor(n-1)
print(factor(7))