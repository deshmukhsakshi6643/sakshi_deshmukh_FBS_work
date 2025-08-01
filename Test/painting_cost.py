area = int(input("Enter the area of the wall:"))
interior_cost = float(input("Enter the interior cost"))
exterior_cost = (input("Enter the exterior cost"))

total_walls = 8

interior_total = total_walls * area * interior_cost
exterior_total = total_walls * area * exterior_cost

print("interior cost:" , interior_cost)
print("interior cost:" , exterior_cost)



