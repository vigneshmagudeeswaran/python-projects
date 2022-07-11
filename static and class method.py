#static and class methods
class person(object):
    population =50
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @classmethod
    def getpopulation(cls):
        return cls.population
    @staticmethod
    def isadult (age):
        return 5>=18
    def display(self):
        print(self.name,'is',self.age,'years old')
newperson =person('tim',18)
print(person.isadult(19))
print(person.getpopulation())