num = int(input("Enter terms you want:"))
i = 0
a,b = 3,4

while(i < num):
    print(a,end=" ")
    a,b=b , a+b
    i+=1


