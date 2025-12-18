#Information Formatter
#Write a Python program that takes user name, age, and salary as input, converts them into appropriate datatypes, 
# and prints the information using proper string formatting.

# takes user name, age, and salary as input
name= input(" Enter your name:")  #  Taking User name
age=int(input(" Enetr your age:")) # user age 
salary=float(input("Enter your salary:"))# user salary

#---------------------------------#
# print user information 
print(f"Hello everyone,this is {name}")
print(f" my age is: %d"% age) # %d  represents Integers
print(f" my salary is:${salary:.2f}") #%.< no.of digits>f Floating point numbers with a fixed 
                                                #amount of digits to the right of the dot.
