#write a python program that will have usecase of school having 10 student 
#and we have to find out that student 
#whose name is the same with another student
#but sur-name is different
student=[ ("pavithra","gaddam"),
         ("sweety" ,"bura"),
          ("swetha"," abbu"),
          (" varshu","eggi"),
          (" pavi","pilli"),
          (" sruthi","mekala"),
          ("varshi", "koti"),
          (" varshu", "yadav"),
          (" swetha","reddy"),
          ("pavithra"," varma"),
          ]

def find_duplicates(students): #find_duplicates that takes a list of students as input.

    students_dict = {}
    duplicates = []

    for first_name, surname in students:  #This is a loop that iterates over the students list
        if first_name in students_dict:     # This checks if the first_name is already a key in the students_dict dictionary.

           
            if surname != students_dict[first_name]:  # this checks if the current surname is different from the one stored in the dictionary.
                
                if (first_name, surname) not in duplicates:  #This checks if the current (first_name, surname)  is not already in the duplicates list.
                    duplicates.append((first_name, surname))
               
                if (first_name, students_dict[first_name]) not in duplicates:  
                    duplicates.append((first_name, students_dict[first_name]))
        else:
            students_dict[first_name] = surname

    return duplicates
   

duplicates = find_duplicates(student)

print("Students with the same first name but different surnames:") # output statement
for first_name, surname in duplicates:
    print(f"{first_name} {surname}")

