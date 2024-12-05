grocery = input("Did you buy a grocery (yes/ no) : ")

if grocery.lower == "yes" :
	item = input("Name of the item: ")
	price = eval(input("Price of the item:" ))
	age = eval(input("Age: "))
	given = eval(input("Amount given: "))
	tax = price * 0.123
	total = price + tax
	
	if age >= 60 :