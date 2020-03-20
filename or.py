name = input("Enter your name: ")
age = input("Enter your age: ")

def fun(age):
    if int(age) % 10 == 1:
        return "godinu"
    elif int(age) % 10 == 2 or int(age) % 10 == 3 or int(age) % 10 == 4:
        return "godine"
    else:
        return "godina"

mrmr = f"{name} ima {age} {fun(age)}"
print(mrmr)