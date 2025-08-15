num = int(input("Enter three digit number:"))
if 100 <= num <= 999:
    first  = num // 100
    second = (num // 10) % 10
    third = num % 10

    if first == 2 * second and second == 2 * third:
        print("Yes , you have done it")
    else:
        ("please try next time")
else:
    print("Not a 3 digit number")



