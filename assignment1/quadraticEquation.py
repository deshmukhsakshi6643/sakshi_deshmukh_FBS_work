a = int(input("Enter value of  a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

sqrt = ((b**2)-(4*a*c))
res1 = (-b-sqrt**0.5)/2*a
res2 = (-b+sqrt**0.5)/2*a

print(f'First  root is{res1} , Second root is:{res2}')