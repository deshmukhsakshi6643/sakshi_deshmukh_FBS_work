num = int(input("Enter three digit number:"))

a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
num = num // 10
reverse = (a*100)+ (b*10)+ c

print("Reversed value:",reverse)


