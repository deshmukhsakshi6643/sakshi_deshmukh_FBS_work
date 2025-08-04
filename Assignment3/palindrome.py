num  = int(input("Enter number:"))

if num == int(str(num)[::-1]):
    print("It is palindrome")
else:
    print("It is not palindrome")