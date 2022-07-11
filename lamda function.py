#lambda function
def func(x):
    return x+5
print(func(2))


func2 = lambda x: x+5
print(func2(2)) 

def fun(x):
    func = lambda x:x+5
    return func2(x)+85

func3 = lambda x,y : x+y
print(func3(5,5))

#map and lamda

a =[1,2,3,4,5,6,7,8,9,10]

newlist =list(map(lambda x: x+5,a ))
print (newlist)
newlist2 = list(filter(lambda x: x%2==0 ,a ))
print(newlist2)

