#fibnonsky series
def fibnosky(n):
    if n<=0:
        print('invalid input')
    elif n ==1 :
        return 0
    elif n ==2 :
        return 1
    else:
        return fibnosky(n-1)+fibnosky(n-2)
print(fibnosky(10))
