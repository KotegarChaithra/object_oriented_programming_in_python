#class -> design or blueprint, contains attributes and behaviour (Methods or Functions)
#object -> instance

# class Computer:
#     def config(self):
#         print("i5, 16gb, 1TB")

# comp1 = Computer()

# print(type(comp1))

# output: 
# <class '__main__.Computer'>
#-------------------------------------------------------------------------------------------------------

#if I want to call config() will give error then how to call
# config()#Error

class Computer:
    def config(self):
        print("i5, 16gb, 1TB")

comp1 = Computer()
comp2 = Computer()

#if we want to call a method we need to call the class first 
# Computer.config()#error still
Computer.config(comp1)
Computer.config(comp2)

#another method
comp1.config()
comp2.config()


#output:
# i5, 16gb, 1TB
# i5, 16gb, 1TB
# i5, 16gb, 1TB
# i5, 16gb, 1TB
