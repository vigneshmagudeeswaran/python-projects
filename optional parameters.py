#
 

def func(x): 
	return x **2
call = func(5)
print(call)

def func(x=1): 
	return x **2
call = func()
print(call)

def func(x): 
	return x **2
call = func(6)
print(call) 

def func(word, freq=1):
	print(word*freq)
call = func('tim',3 )

# multiple optional parameters
def func(word, add=5, freq=1):
    print(word*(freq+add)) 
call = func('hello ',0,3)
 
class car(object):
    def __init__(self,make,model,year,condition ='new',kms=0):
        self.make = make
        self.model = model
        self.year= year
        self.condition = condition
        self.kms = kms
    def display (self,showall=True):
            if showall:
                print('This car is a %s %s from %s, it is %s and has %s kms.'%(self.make,self.model,self.year,self.condition,self.kms))
            else:
                print('This car is a %s %s from %s'%(self.make,self.model,self.year))
whip = car('ford', 'fusion', 2012)
whip.display()
            
    