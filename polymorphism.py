# # Duck typing:

# class VSCode:

#     def execute(self):
#         print("Compiling")
#         print("Running")

# class MyEditor:

#     def execute(self):
#         print("Spell chack")
#         print("Convention check")
#         print("Compiling")
#         print("Running")

# class Laptop:

#     def code(self,ide):
#         ide.execute()

# # ide=VSCode()
# ide = MyEditor()

# lap1=Laptop()
# lap1.code(ide)

#output:
# Spell chack
# Convention check
# Compiling
# Running

#---------------------------------------------------------------------------------------------------

# Operator overloading:

# a = 5
# b = 'World'
# print(a+b)

# #error:
# Traceback (most recent call last):
#   File "c:\Users\hp\Documents\Python Codes\OOPS_python\polymorphism.py", line 40, in <module>
#     print(a+b)
#           ~^~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# a = 5
# b = 6

# print(a+b)

# print(int.__add__(a,b))

# #output:
# 11
# 11

# a = '5'
# b = '6'

# print(a+b)

# print(str.__add__(a,b))

# #output:
# 56
# 56

# class Student:

#     def __init__(self, m1,m2):
#         self.m1=m1
#         self.m2=m2

#     def __add__(self,other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)

#         return s3

# s1 = Student(58,69)   #  -> Student.__add__(s1,s2)
# s2 = Student(60,65)


# s3 = s1+s2

# print(s3.m1)

# #output:
# 118


# class Student:

#     def __init__(self, m1,m2):
#         self.m1=m1
#         self.m2=m2

#     def __add__(self,other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1,m2)

#         return s3
    
#     def __gt__(self,other):
#         r1 = self.m1 + self.m2
#         r2 = other.m1 + other.m2
        
#         if r1 > r2:
#             return True
#         else:
#             return False

# s1 = Student(58,69)   #  -> Student.__add__(s1,s2)
# s2 = Student(60,65)


# s3 = s1+s2

# if s1 > s2:
#     print("s1 wins")
# else:
#     print("s2 wins")

# #output:
# s1 wins

class Student:

    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3
    
    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        
        if r1 > r2:
            return True
        else:
            return False
        
    def __str__(self):
        return self.m1, self.m2
    
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(58,69)   #  -> Student.__add__(s1,s2)
s2 = Student(60,65)


s3 = s1+s2

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")


a = 9 
print(a.__str__()) #--> a.__str__()

print(s1.__str__())

print(s1)

#output:
# s1 wins
# 9
# <__main__.Student object at 0x0000014CEC12AF60>

#output:
# s1 wins
# 9
# (58, 69)

