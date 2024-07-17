class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()

    def show(self):
        print(s1.name , s1.rollno)
        self.lap.show()

    class Laptop:
        
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student("Chaithra",10)
s2=Student("Divya",15)

s1.show()

lap1=s1.lap
lap2=s2.lap

print(id(lap1))
print(id(lap2))
