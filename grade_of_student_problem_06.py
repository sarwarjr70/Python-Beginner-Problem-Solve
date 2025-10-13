marks = input("Enter your marks: ")

if (marks >= '80') and (marks <= '100'):
    Grade = 'A+'
elif (marks >= '70') and (marks < '80'):
    Grade = 'A'
elif (marks >= '60') and (marks < '70'):
    Grade = 'A-'
elif (marks >= '50') and (marks < '60'):
    Grade = 'B'
elif (marks >= '40') and (marks < '50'):
    Grade = 'C'
else:
    Grade = 'F'
print("Your Grade is:", Grade)