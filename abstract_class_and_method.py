# from abc import ABC, abstractmethod

# class Computer(ABC):

#     @abstractmethod
#     def process(self):
#         pass

# com = Computer()
# com.process()


# #if i use abstract class then I can't create object of it.

# #--------------------------------------------------------------------------------

# from abc import ABC, abstractmethod

# class Computer(ABC):

#     @abstractmethod
#     def process(self):
#         pass

# class Laptop(Computer):
#     pass

# # com = Computer()
# com1 = Laptop()
# # com.process()

# #-----------------------------------------------------------------------------
# from abc import ABC, abstractmethod

# class Computer(ABC):

#     @abstractmethod
#     def process(self):
#         pass
# class Laptop(Computer):
#     def process(self):
#         print("Running")
# # com = Computer()
# com1 = Laptop()
# # com.process()
# com1.process()

# #output:
# Running

#----------------------------------------------------------------

from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Running")
        
class Whiteboard(Computer):
    def write(self):
        print("It's writing")

class Programmer:
    def work(self,com):
        print("Solvig Bugs")
        com.process()

# com = Computer()
com1 = Laptop()
com2= Whiteboard()
# com.process()
com1.process()

prog1 = Programmer()
prog1.work()