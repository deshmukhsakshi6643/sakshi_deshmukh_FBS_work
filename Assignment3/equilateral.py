a = int(input("Enter 1 sides:"))
b = int(input("Enter 2 sides:"))
c = int(input("Enter 3 sides:"))

if(a == b == c):
    print("Equilateral triangle.")
elif(a == b or b == c or a == c):
    print("Isosceles triangle.")
else:
    print("Scelene triangle.")