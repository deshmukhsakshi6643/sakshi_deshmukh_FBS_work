amt = int(input("Enter amount to calculate min no.of notes:"))
temp = amt

two_thousands = temp // 2000
temp = temp % 2000

fifty_hundreds= temp // 500
temp = temp % 500

hundred = temp // 100
temp = temp % 100

fifty = temp // 50
temp = temp % 50

twenty = temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10

total_notes = two_thousands + fifty_hundreds + hundred + fifty + twenty + ten

print(f'total_notes:{total_notes}')
