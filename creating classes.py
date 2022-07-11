class Dog(object):
    def __init__(self,name,age):
        self.name =name
        self.age =age 
        print('nice you made a dog')
    def speak(self):
        print("hi i am ", self.name,'and i am', self.age,'years old')
    def changeage(self,age):
        self.age = age 
    def add_weight(self,weight):
        self.weight = weight
tim = Dog('tim',55)
fred = Dog('fred',3)
tim.speak()
fred.speak()
tim.changeage(66)
tim.speak()
print(tim.age)
print(tim.name)
# we cam create multiple object of class 
tim.add_weight(82)
print(tim.weight)