print("two number below")
a=int(input("enter first number:"))
b= int(input("enter second number;"))
ch=0
while ch<5:
    print("cacalculator menu")
    print(" 1.add")
    print("2.subtract")
    print("3.multiplication")
    print("4.devision")

    ch=int(input("enter choice:"))
    if ch==1:
        c=a+b
        print("sum:",c)
    elif ch==2:
        c=a-b
        print("difference;",c)
    elif ch==3:
        c=a*b
        print(" product :",c)
    elif ch==4:
        c=a/b
        print(" division:",c)
    else:
        print(" wrong")
    