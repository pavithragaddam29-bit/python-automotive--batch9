s= input(" enter the string:")
vowels="AEIOUaeiou"
count=0
for char in s:
     if char in vowels:
        count=count+1
        print(" no.of vowels:",count)
        
    