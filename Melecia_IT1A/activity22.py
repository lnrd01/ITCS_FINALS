#Creating a function

from unicodedata import name


def activity1():
    print("Hello World")

def activity2():
    print("Hello World \nHello BSIT 1A")    

def activity3():
    name = input("Enter your full name: ")
    gap = input("Enter your age: ")
    gender = input("Enter your gender: ")
    bday = input("Ent-er your Birthdate : ")
    birthplace = input("Enter your birthplace: ")
    address = input("Enter your address: ")
    m_name = input("Enter your mother's name: ")
    f_name = input("Enter your father's name: ")
    heigth = input("Enter your height: ")
    weight = input("Enter your weight :")
    civil = input("Enter your civil status: ")
    religion = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")

    print("hello, my name is", name , "a",  )

def activity4():
    num1 = eval(input("Enter a number"))
    num2 = eval(input("Enter another number"))

    answer = num1 + num2

    print("the sum of", num1, "+", num2, "is", answer)

    
def activity5():
    print("FAHRENHEIT TO CELSUIS CONVERTER PROGRAM")
    print("=======================================")
    fh = eval(input("Enter temperature in fahrenheit ---> "))
    cl = ((fh - 32) * 5) / 9
    print(f"{fh} degrees fahrenheit converted to celsuis is {round(cl, 2)} ")

def activity6():
    x = 5
    print(x),
    x = x + 10
    print(x)
    x = x + 15
    print(x)
    x += 10
    print(x)

def activity7():
    gold = 0
    miner = input("Hi, what is your name? ")
    isGold = input("is the mineral gold? ")
    if isGold.lower() == "yes" :
        gold += 1
        print(f"Hi {miner}, the total number of your gold is {gold}")
    else:
        print(f"Hi {miner}, the total number of your gold is {gold}")

def activity8():
    
    password = input("Enter your password: ")

    if password.lower() == "secret" :
	    print("Access Granted")
	    print("Enjoy the System")

    elif password.lower() == "pogiako123" :
	    print("Access Granted")
	    print("Enjoy the System")

    elif password.lower() == "gagawinko123" :
	    print("Access Granted")
	    print("Enjoy the System")

    else:
	    print("Access Denied")

    print("System Exit")

def activity9():
    pass

def activity10():
    pass

def activity11():
    pass

def activity12():
    pass

def activity13():
    pass

def activity14():
    pass

def activity15():
    pass


def activity16():
    pass


def activity17():
    pass


def activity18():
    pass


def activity19():
    pass



activity4()