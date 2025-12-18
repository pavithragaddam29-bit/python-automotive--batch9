# ATM simulation
print(" : Please insert you card :") # card insertion
pin=input(" enter your pin:") # pin verification
if len(pin)!= 4:
  print(" Invalid pin")
  exit()

balence=5000 #  starting amouunt in the account
while True:
    # instructions about services
    print(" ATM service:")
    print(" 1.check balence")
    print("2. Diposit money")
    print("3. withdraw money")
    print("4. exit")

    choice=input("Enter your choice:") # choosing choice
  
    if choice=='1': # To check the balence
      print(" your current balence:", balence) 
    elif choice=='2': # To Deposite money
      Amount=int(input("Enter the amount to deposit"))
      balence= balence+Amount
      print(" amount deposited succesfully")
    elif choice=='3': # To withdraw money
      amount= int(input(" enter amount to withdraw:"))
      if amount<= balence:
        balence=balence-amount 
        print(" Amount withdrawn succesfully")
      else:
        print(" Insufficiant balence,try again")
    elif choice=='4': # To exit
       print("Thank you,welcome again")
    else:
       print("invalid choice,try again") 
