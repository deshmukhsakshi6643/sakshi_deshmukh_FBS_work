s1 = int(input("Enter marks of subject 1:"))
s2 = int(input("Enter marks of subject 2:"))
s3 = int(input("Enter marks of subject 3:"))
s4 = int(input("Enter marks of subject 4:"))
s5 = int(input("Enter marks of subject 5:"))

total_marks = s1 + s2 + s3 + s4 + s5

average = (total_marks / 500) * 100
print(f'Percentage:{average}')

if(average >= 85):
    print("First class Distinction")
elif(average >= 75):
    print("Second class Distinction")
elif(average >= 65):
    print("Third class Distinction")
elif(average >= 55):
    print("Pass")
else:
    print("Fail")