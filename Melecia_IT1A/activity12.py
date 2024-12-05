
n1 = 0
odd = 0
even = 0
for m in range(1, 10):
    n2 = eval(input(f"Enter a number {m}: "))
    n1 += n2
    if n2 % 2 == 0:
        even += n2
    else:
        odd += n2

print(f"The total of the number you entered is {n1}")
print(f"The total of the number you entered is {odd}")
print(f"The total of the number you entered is {even}")