name = input("Enter your name: ")

student = input("Are you a student of DLL (yes/ no) : ")

if student.lower() == "yes" :
	yearlevel = input("What year level are you? \n F - Freshmen  \n S - Sophomore \n J -Junior \n R - Senior \nYour answer: ")
	if yearlevel.lower() == "f" :
		print(f"Hello {name}, you're a freshmen, welcome to DLL")

	elif yearlevel.lower() == "s" :
		print(f"Hello {name}, you're a sophmore, welcome to DLL")

	elif yearlevel.lower() == "j" :
		print(f"Hello {name}, you're a junior, welcome to DLL")

	elif yearlevel.lower() == "r" :
		print(f"Hello {name}, you're a senior, welcome to DLL")

else :
	print("Thank you for using the system")