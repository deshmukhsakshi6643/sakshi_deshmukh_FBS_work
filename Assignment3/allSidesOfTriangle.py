a1 = int(input("Enter 1 sides:"))
a2 = int(input("Enter 2 sides:"))
a3 = int(input("Enter 3 sides:"))

if((a1 + a2 > a3) and (a1 + a3 > a2) and (a2 + a3 > a3)):
    print("Valid triangle.")
else:
    print("Invalid triangle.")
    