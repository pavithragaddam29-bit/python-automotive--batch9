# set data type
myset={'apple', 'banana', 'pomegranet','apple',False,0,2}
mylist=['a','b','c']
myset2={'a','n'}
print(myset)
empty_set=set()
empty_dict={}
print(type(empty_set))
myset.add(101)
myset.discard('apple')
myset.update(mylist)
count=len(mylist)
print(myset|myset2) #union
print(myset&myset2)#interaction
for fruit in myset:
     print( fruit)
#True=1
#False=0
"banana" in myset
" grapes" in myset