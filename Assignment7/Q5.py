n=5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i +1):
        if(i==n or j==1 or j==i):
            print(j, end = " ")
        else:
            print("  ", end="")
    print()