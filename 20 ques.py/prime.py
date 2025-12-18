num= int ( input("enter a number:")) 
for i in range(2,num): # condition
    if num % i==0:
        print(num,"not a prime number")
        break
    else:
         print (num," is a prime number")