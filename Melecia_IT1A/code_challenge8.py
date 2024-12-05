prelim = eval(input("Enter your score in prelim: "))
midterm = eval(input("Enter your score in midterm: "))
semi_final = eval(input("Enter your score in semi-final: "))
final = eval(input("Enter your score in final: "))
quiz = eval(input("Enter your score in quiz: "))
project = eval(input("Enter your score in project grade: "))

fg = (prelim * .15) + (midterm * .15) + (semi_final * .15) + (final * .15) + (quiz * .25) + (project * .15)

print("Your final grade is" , fg)
if fg >= 75 :
	print("You passed the course")
	print("Congratulations")

else:
	print("Sorry, you failed")


