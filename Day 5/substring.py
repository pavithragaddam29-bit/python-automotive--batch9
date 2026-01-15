mystring="abcdef  ghijkl"
sub1=mystring[0:6] # slice the first 7 elements
sub2=mystring[7: ]# From the 7th element till end
sub3=mystring[ :5] # first 6 elements
sub4=mystring[10]# the 10th element-index from 0
sub5=mystring[-5]# last 5 elements
if "a" in mystring:
  print(" a is there")
word=mystring.split(" ")
print(word)
mystring.upper()
mystring.lower()
