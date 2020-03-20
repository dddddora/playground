print("hello world")

a = "This is a string"
b = 6 #this is an integer

h = """This is a multi-line string.
This is the second line
This is the third line"""

age = 21
name = "Tom"

c = name + " ima " + str(age) + " godinu"
d = "{0} ima {1} godinu".format(name,age)
e = f"{name} ima {age} godinu"
print(c)
print(d)
print(e)



print("Please enter your name")
name = input()

age = input("Please enter your age: ")

g = f"{name} ima {age} "
print(g)