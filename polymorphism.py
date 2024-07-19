# Duck typing:

class VSCode:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell chack")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()

# ide=VSCode()
ide = MyEditor()

lap1=Laptop()
lap1.code(ide)

#output:
# Spell chack
# Convention check
# Compiling
# Running

#---------------------------------------------------------------------------------------------------

# Operator overloading:

