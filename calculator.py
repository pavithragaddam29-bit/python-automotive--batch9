print("two number below")
a=int(input("enter first number:"))
b= int(input("enter second number;"))
ch=0
while ch<5:
    print("cacalculator menu")
    print(" 1.add")
    print("2.subtract")

    ch=int(input("enter choice:"))
    if ch==1:
        c=a+b
        print("sum:",c)
    elif ch==2:
        c=a-b
        print("difference;",c)
    else:
        print(" wrong")
    
