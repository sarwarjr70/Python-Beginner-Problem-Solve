marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))
total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 300) * 100

if (percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("Student is Pass with percentage:", percentage)
else:
    print("Student is Fail with percentage:", percentage)

# if(percentage >= 90):
#     print("Grade A")
# elif(percentage >= 80):
#     print("Grade B")
# elif(percentage >= 70):
#     print("Grade C")
# elif(percentage >= 60):
#     print("Grade D")
# elif(percentage >= 40):
#     print("Grade E")
# else:
#     print("Grade Fail", percentage)    