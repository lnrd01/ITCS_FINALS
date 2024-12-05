print("FAHRENHEIT TO CELSIUS CONVERTER PROGRAM")
print("=======================================")

fh = eval(input("Enter temperature in fahrenheit ---> "))

cl = ((fh - 32) * 5) / 9

print(f"{fh} degrees fahrenheit converted to celsuis is {round(cl, 2)} ")
