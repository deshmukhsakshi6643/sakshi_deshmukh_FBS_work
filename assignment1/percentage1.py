m1 = int(input("Enter marks of English:"))
m2 = int(input("Enter marks of Chemistry:"))
m3 = int(input("Enter marks of Marathi:"))
m4 = int(input("Enter marks of Physics:"))
m5 = int(input("Enter marks of Zoology:"))

gain_marks = m1 + m2 + m3 + m4 + m5

percentage = (gain_marks / 500)*100
print(f"Percentage is {percentage}%:")