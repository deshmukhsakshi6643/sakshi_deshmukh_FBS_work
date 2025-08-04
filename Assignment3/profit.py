cp = float(input("Enter cost prize:"))
sp = float(input("Enter selling prize:"))

if(sp > cp):
    print("Profit")
elif(cp < sp):
    print("Loss")
else:
    print("Not profit,Not loss")