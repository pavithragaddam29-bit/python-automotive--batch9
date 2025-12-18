# reverse srting
string=input("  enter the string:")
reverse=""
for i in range(len(string)):
    reverse=string[i]+reverse
    print(reverse)