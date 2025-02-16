# Input number of students in a class
def count_number_student():
    num_stu = int(input("Enter number of students: "))
    return num_stu


# Input students information
def get_student_info(num_stu):
    student_info = []
    for i in range(0,num_stu):
        id = input("Enter id of the student {}: ".format(i+1))
        name = input("Enter name of the student {}: ".format(i+1))
        birth = input("Enter the date of birthday of the student {}: ".format(i+1))
        student_info.append([id, name, birth])
    return student_info

# Input number of courses
def count_number_course():
    num_course = int(input("Enter number of courses: "))
    return num_course


# Input courses information
def get_course_info(num_course):
    course_info = []
    for i in range(0,num_course):
        id = input("Enter id of the course {}: ".format(i+1))
        name = input("Enter name of the course {}: ".format(i+1))
        course_info.append([id, name])
    return course_info

# Select a course, input marks for student in this course
def select_course(student_info, course_info):
    # Create a list of marks of students in each course by 2d list, 
    # number of rows = number of courses, number of columns = number of students
    list_mark_course = [[None for i in range(len(student_info))] for j in range(len(course_info))]
    while True:
        print("Select a course to input marks: ")
        for i in range(len(course_info)):
            print("Course {}: {}".format(i+1, course_info[i][1]))
        select = int(input("Enter the number of the course you want to choose: "))
        if select > len(course_info) or select < 1:
            print("Invalid choice. Please try again.")
        else:  
            print("You have selected course: ", course_info[select-1][1], " (", course_info[select-1][0], ")")          
            for i in range(len(student_info)):
                mark = int(input("Enter mark of {}: ".format(student_info[i][1])))
                list_mark_course[select-1][i] = mark
        print("Enter 0 to stop. Enter other number to continue.")
        if int(input("Enter your choice: ")) == 0:
            break        
    return list_mark_course, course_info, student_info


def main():
    num_stu = count_number_student()
    student_info = get_student_info(num_stu)
    num_course = count_number_course()
    course_info = get_course_info(num_course)
    list_mark_course, course_info, student_info = select_course(student_info, course_info)
    print("")
    print("")
    print("List of marks of students in each course:")
    for i in range(len(course_info)):
        print("Course: ", course_info[i][1], " (", course_info[i][0], ")" )
        for j in range(len(student_info)):
            print("     Student: ", student_info[j][1])
            print("     ID: ", student_info[j][0])
            print("     Date of birth: ", student_info[j][2])
            print("     Mark: ", list_mark_course[i][j])
            print("")
main()

        

