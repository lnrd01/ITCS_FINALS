for a in range(1,6):
    for b in range(6, a, -1):
        print(" ", end=" ")
    for c in range(1, a+1):
        print("*", end=" ")  
    for d in range(1, a):
        print("*", end=" ")                 
    print()    

for x in range(1,6):
    for y in range(1, x+1):
        print(" ", end=" ")
    for z in range(6, x+1, -1):
        print("*", end=" ")    
    for m in range(6, x, -1):
        print("*", end=" ")        
    print()    

