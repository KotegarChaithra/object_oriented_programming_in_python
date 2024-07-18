class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):

    def __init__(self):
        super().__init__()#if we don't specify super the 'B' cunstroctur calls only B init.
        print("in B Init")#if we only want B Init then don't specify super() and use B() constructor

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

a1=B()

#output:
in A Init
in B Init

#-----------------------------------------------------------------
class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")

class B(A):

    def __init__(self):
        super().__init__()#if we don't specify super the 'B' cunstroctur calls only B init.
        print("in B Init")#if we only want B Init then don't specify super() and use B() constructor

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")

# mutiple inheritence starts from left to right, even if we have 2 super class it is biased towards "A" class, hence we use Method Resolution Order (MRO)
class C(B): 

    def __init__(self):
        super().__init__()
        print("in C Init")

    def feat(self):
        super().feature2()

    

a1=C()
a1.feat()

#output:
in A Init
in B Init
in C Init
Feature 2 working