





 


class Student:

  def __init__(self, name, roll_number, cgpa): 
    self.name = name
    self. roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):

# Sort the list of students in descending orders of cgpa

sorted_students = sorted(student_list, key=lambda Student: Student.cgpa,reverse=True)

#syntax - lambda arg:exp
return sorted_students


# example
Students = [Student("Abi","AB1",7.8),
            Student("Ram","AB2",8.9),
            Student("Mani","AB3",9.1),
            Student("Abar","AB4",9.9),]
Sorted_Students = Sort_Students(Students)
# print
for Student in Sorted_Students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(Student.name,Student.roll_number,Student.cgpa))