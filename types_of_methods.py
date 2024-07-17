#3 types 0f methods are:
#--Instance method
#--Class method
#--Static method

#instance method
# class Student():

#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3

# s1 = Student(34,47,32)
# s2=Student(89,92,12)

# print(s1.avg())
# print(s2.avg())

# #output:
# 37.666666666666664
# 64.33333333333333
#------------------------------------------------------------------------------------
# class Student():

#     schools = "Telusko"

#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
#     #accessors
#     def get_m1(self):
#         return self.m1 
#     #mutator
#     def set_m1(self,value):
#         return self.m1=value

# s1 = Student(34,47,32)
# s2=Student(89,92,12)

# print(s1.avg())
# print(s2.avg())

#--------------------------------------------------------------------------------------------------
#Class method
# class Student():

#     school = "Telusko"

#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
    
#     @classmethod # decorator should be used other wise we will get error for class method
#     def info(cls):
#         return cls.school

# s1 = Student(34,47,32)
# s2=Student(89,92,12)

# print(s1.avg())
# print(s2.avg())
# print(Student.info())

# #output:
# 37.666666666666664
# 64.33333333333333
# Telusko

#------------------------------------------------------------------------------------------------------
#static method
class Student:

    school = "Telusko"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m1)/3
    
    @classmethod
    def getSchool(cls):
        return cls.school
    
    #staticmethod
    def info():
        print("This is student class.. in abc module")
    
s1 = Student(34,47,32)
s2=Student(89,92,12)

print(s1.avg())
print(Student.getSchool())

Student.info()
