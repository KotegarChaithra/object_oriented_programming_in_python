class Computer:

    def __init__(self):
        self.name="Chaithra"
        self.age=24

c1 = Computer()
c2 = Computer()

#Objects are stored in Heap memory, wherever we create different objects it will create different memory space
print(id(c1))
print(id(c2))

#output:
# 2661988869104
# 2661988869152

#--------------------------------------------------------------------------------------------------------

class Computer:
    def __init__(self):
        self.name="Chaithra"
        self.age=24

c1=Computer()
c2=Computer()

# Print the same names 
print(c1.name)
print(c2.name)

#output:
# Chaithra
# Chaithra
#-------------------------------------------------------------------------------------------------------------------------
#If I want to change the one of name how can I do that
class Computer:

    def __init__(self):
        self.name="Chaithra"
        self.age = 24

c1 = Computer()
c2 = Computer()

#To change the name there are 2 methods one of the method is this:
c1.name="Divya"
c1.age=25
print(c1.name)
print(c2.name)

#output:
# Divya
# Chaithra

#-------------------------------------------------------------------------------------------------------------------------

class Computer:

    def __init__(self):
        self.name="Chaithra"
        self.age=24

    def update(self):
        self.age=25

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1=Computer()
c2=Computer()

if c1.compare(c2):
    print("They are same")

print(c1.name)
print(c1.age)

#output:
# They are same
# Chaithra
# 24

#--------------------------------------------------------------------------------------------------------------------------

class Computer:

    def __init__(self):
        self.name="Chaithra"
        self.age=24

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
        
c1 = Computer()
c1.age=30
c2=Computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.age)
print(c2.age)

#output:
# They are different
# 30
# 24
