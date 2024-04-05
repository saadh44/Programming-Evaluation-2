####INPUT####
course1 = int(input( "Enter the first course grade: "))
course2 = int(input( "Enter the second course grade: "))
course3 = int(input("Enter the third course grade: "))
course4 = int(input("Enter the fourth course grade: ")) 

average = (course1 + course2 + course3 + course4) / 4
letter_grade = ""

####PROCESS####}
if average >= 95:
  letter_grade = "A+"
elif average >= 87:
  letter_grade = "A"
elif average >= 80:
  letter_grade = "A-"
elif average >= 77:
    letter_grade = "B+"
elif average >= 72:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "B-"
elif average >= 67:
    letter_grade = "C+"
elif average >= 63:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "C-"
elif average >= 57:
    letter_grade = "D+"
elif average >= 54:
    letter_grade = "D"
elif average >= 50:
    letter_grade = "D-"
else:
    letter_grade = "F"

####OUTPUT####
print("The average is " + str(average) , "." + " This is considered " + letter_grade)
