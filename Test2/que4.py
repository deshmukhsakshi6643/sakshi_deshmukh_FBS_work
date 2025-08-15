height = int(input("Enter height:"))
width = int(input("Enter width:"))

total_walls = 4
area = height * width 

interior_cost = total_walls * area

print("Cost of Painting:" , interior_cost)