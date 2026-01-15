print(" Get max,Get min,swap value of variable")
print(" \n 1. Max \n 2.Min \n 3. Swap")
a,b= map( int,input(" enter two numbers"). split(",")) 
choice=int(input(" enter your choice"))
if (choice ==1):
      print(max(a,b))
elif (choice==2):
      print(min(a,b))
elif(choice==3):
      a,b=b,a
      print(" After swapping %d %d" %(a,b))
    
else: 
      print(" invalid choice")