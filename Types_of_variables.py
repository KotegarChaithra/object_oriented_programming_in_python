#2 types of variables
#-- Instance variable
#-- Class(Static) variable

class Car:

    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=Car()
c2=Car()

#changing value
c1.mil=8

print(c1.mil,c1.com)
print(c2.mil,c2.com)

#output:
# 8 BMW
# 10 BMW
#-------------------------------------------------------------------------------------------------------------------------
class Car:
    wheel=4 #class variable or class name spance

    def __init__(self):
        self.mil=10 #instance variable or instance namespace
        self.com="BMW" #instance variable or instance namespace

c1=Car()
c2=Car()

c1.mil=8

Car.wheel=5 #changing class variable value

print(c1.mil,c1.com,c1.wheel)
print(c2.mil,c2.com,c2.wheel)  

# #output:
# 8 BMW 5
# 10 BMW 5