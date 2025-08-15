num = int(input("Enter number:"))
i = 2
while(i  >  num):
    print(num % i == 0)
    i = i + 1
print(f'Prime number is:{i}')