students=[90,80,60,67,54,56,100]
pass_students=[ i if i>=60 else" failed" for i in students]
print(pass_students)