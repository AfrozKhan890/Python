def Input_Student_Detail():
    Students = []
    Number_Students = int(input("Enter the number of Students: "))

    for _ in range(Number_Students):
        name = input("Enter Student's Name: ")
        
        Number_Subjects = int(input(f"Enter the number of subject for {name}: "))

        Subjects_Grades = []
        for _ in range(Subjects_Grades):
            subject = input("Enter Student's Name: ")
            grade  = float(input(f"Enter Marks of {subject}"))
            Subjects_Grades.append(subject,grade)
        Students.append(name, Subjects_Grades)
    return Students

def Calculate_Average(Student):
    Subject_Grades = Student[1]
    total = sum(grade for Subject, grade in Subject_Grades)
    Average = total/len(Subject_Grades)
    return Average

def Status(Average):
    if(Average>= 85):
        return "Distinction"
    elif(Average>=50):
        return "Pass"
    else:
        return "Fail"

def Student_Result(Students):
    for Student in Students:
        name, Subjects_Grade = Student
        print(f"\nStudent: {name}")
        for Subject, grade in Subjects_Grade:
            print(f"{Subject}: {grade}")
        average = Calculate_Average(Student)
        Status = Student_Result(average)

        print(f"Average Grade: {average:.2f}")
        print(f"Status: {Status}")

# Main function
def main():
    students = Input_Student_Detail()
    Student_Result(students)

if __name__ == "__main__":
    main()
