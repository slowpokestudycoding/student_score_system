
import re
import os

filename = "students.txt"  # Name the file that saves student information


def menu():
    # output menu
    print('''
        Student Scores System
        ---------- Menu -----------------------   
                                                 
        1 Add student information                
        2 Find student information               
        3 Delete student information            
        4 Revise student information                                
        5 Ranking                                
        6 Count the number of student            
        7 Show all students information          
        0 Leave this system                      
       -----------------------------------------
        Please enter a number to select menu    
    ''')


def main():
    ctrl = True  # Flag to indicate whether to exit the system
    while (ctrl):
        menu()  # show menu
        option = input("Enter a number：")  # select the menu
        option_str = re.sub("\D", "", option)  # extract the number
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:  # leave system
                print('You leave student score system！')
                ctrl = False
            elif option_int == 1:  # Add student information
                insert()
            elif option_int == 2:  # Find student information
                search()
            elif option_int == 3:  # Delete student information
                delete()
            elif option_int == 4:  # Revise student information
                modify()
            elif option_int == 5:  # Ranking
                sort()
            elif option_int == 6:  # Count the number of student
                total()
            elif option_int == 7:  # Show all students information
                show()


'''1 Add student information'''


def insert():
    stdentList = []        # the list of saving student information
    mark = True  # Do you want to continue adding?
    while mark:
        id = input("Please enter a ID（Example: 1001）：")
        if not id:  # ID is none,break the loop
            break
        name = input("Please enter a name：")
        if not name:  # name is none,break the loop
            break
        try:
            english = int(input("Please enter English score："))
            python = int(input("Please enter Chinese score："))
            chinese = int(input("Please enter Python score："))
        except:
            print("enter is wrong, it's not a number...Please enter the information again.")
            continue
        stdent = {"id": id, "name": name, "english": english, "python": python, "chinese": chinese}  # Save the inputted student information to a dictionary
        stdentList.append(stdent)  # add student dictionary into the list
        inputMark = input("continue to add more information？（y/n）:")
        if inputMark == "y":  # keep adding information
            mark = True
        else:  # don't keep adding information
            mark = False
    save(stdentList)  # save student information into the file
    print("student information saved successfully！！")


# save students information to the file
def save(student):
    try:
        students_txt = open(filename, "a")
    except Exception as e:
        students_txt = open(filename, "w")  # If the file does not exist, create a new file and open it
    for info in student:
        students_txt.write(str(info) + "\n")  # Store in lines, add newline characters.
    students_txt.close()  # close the file


'''2 Find student information'''


def search():
    mark = True
    student_query = []  # Save the query results of the student list
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename):  # Check if the file exists
            mode = input("To search by ID, please enter 1. To search by name, please enter 2.：")
            if mode == "1":
                id = input("Please enter student ID:")
            elif mode == "2":
                name = input("Please enter student name：")
            else:
                print("Your input is incorrect. Please enter again!")
                search()  # research
            with open(filename, 'r') as file:  # open the file
                student = file.readlines()  # read the file
                for list in student:
                    d = dict(eval(list))  # turn str to dictionary
                    if id is not "":  # Check if the search is based on ID
                        if d['id'] == id:
                            student_query.append(d)  # Save the found student information to the list
                    elif name is not "":  # Check if the search is based on name.
                        if d['name'] == name:
                            student_query.append(d)  # Save the found student information to the list
                show_student(student_query)  # Display the search results
                student_query.clear()  # clear list
                inputMark = input("Do you want to continue the search?（y/n）:")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("there is no information here...")
            return


'''3 Delete student information'''


def delete():
    mark = True  # Flag whether it is within the loop
    while mark:
        studentId = input("Please enter the the student ID you want to delete:")
        if studentId is not "":  # Check if the student information to be deleted exists
            if os.path.exists(filename):  # Check if the file exists
                with open(filename, 'r') as rfile:  # open the file
                    student_old = rfile.readlines()  # read all information in the file
            else:
                student_old = []
            ifdel = False  # mark has been deleted or not
            if student_old:  # if student information exists
                with open(filename, 'w') as wfile:  # use writing model to open the file
                    d = {}  # define a blank dictionary
                    for list in student_old:
                        d = dict(eval(list))  # turn str to dictionary
                        if d['id'] != studentId:
                            wfile.write(str(d) + "\n")  # Write a student information entry to the file
                        else:
                            ifdel = True  # mark has been deleted
                    if ifdel:
                        print("The student information for ID %s has been deleted..." % studentId)
                    else:
                        print("No student information was found for ID %s..." % studentId)
            else:  # The student's information does not exist
                print("can't find the student information...")
                break  # break loop
            show()  # show all students information
            inputMark = input("Do you want to continue deleting the information?(y/n):")
            if inputMark == "y":
                mark = True  # continue deleting
            else:
                mark = False  # leave delete student information function


'''4 Revise student information'''


def modify():
    show()  # show all student information
    if os.path.exists(filename):  # Check if the file exists
        with open(filename, 'r') as rfile:  # open the file
            student_old = rfile.readlines()  # read all information in the file
    else:
        return
    student_id = input("Please enter the ID of the student you want to modify:")
    with open(filename, "w") as wfile:  # use writing model to open the file
        for student in student_old:
            d = dict(eval(student))  # turn str to dictionary
            if d["id"] == student_id:  # Confirm if this is the student whose information you want to modify
                print("The student has been found. You can modify their information!")
                while True:  # enter the information you want to revise
                    try:
                        d["name"] = input("Please enter the name:")
                        d["english"] = int(input("Please enter English score:"))
                        d["chinese"] = int(input("Please enter Chinese score:"))
                        d["python"] = int(input("Please enter Python score:"))
                    except:
                        print("Your input is incorrect. Please enter again.")
                    else:
                        break  # break loop
                student = str(d)  # turn dictionary to str
                wfile.write(student + "\n")   # Write the modified information to the file
                print("Revise successfully！")
            else:
                wfile.write(student)  # Write the unmodified information to the file
    mark = input("Do you want to continue modifying other student information?？(y/n)：")
    if mark == "y":
        modify()  # Re-execute the modification action


'''5 ranking'''


def sort():
    show()  # show all student information
    if os.path.exists(filename):  # Check if the file exists
        with open(filename, 'r') as file:  # open the file
            student_old = file.readlines()  # read all information in the file
            student_new = []
        for list in student_old:
            d = dict(eval(list))  # turn str to dictionary
            student_new.append(d)  # Add the converted dictionary to the list
    else:
        return
    asc_or_desc = input("Please choose(0 in ascending order；1 in a descending order):")
    if asc_or_desc == "0":  # in ascending order
        asc_or_descBool = False           # mark the variable to False in descending order
    elif asc_or_desc == "1":  # in descending order
        asc_or_descBool = True          # mark the variable to True in descending order
    else:
        print("Your input is incorrect. Please enter again！")
        sort()  
    mode = input("Please select the sorting method\n(1 Rank according to the english score；2 chinese score；3 python score；0 total score):")
    if mode == "1":  # Rank according to the english score
        student_new.sort(key=lambda x: x["english"], reverse=asc_or_descBool)
    elif mode == "2":  # Rank according to the chinese score
        student_new.sort(key=lambda x: x["chinese"], reverse=asc_or_descBool)
    elif mode == "3":  # Rank according to the python score
        student_new.sort(key=lambda x: x["python"], reverse=asc_or_descBool)
    elif mode == "0":  # Rank according to the total score
        student_new.sort(key=lambda x: x["english"] + x["chinese"] + x["python"], reverse=asc_or_descBool)
    else:
        print("Your input is incorrect. Please enter again！")
        sort()
    show_student(student_new)  # show the ranking


''' 6 calculate the total number of students'''


def total():
    if os.path.exists(filename):  # Check if the file exists
        with open(filename, 'r') as rfile:  # open the file
            student_old = rfile.readlines()  # read all information in the file
            if student_old:
                print("There are %d students here！" % len(student_old))
            else:
                print("Student information has not been saved yet！")
    else:
        print("No information has been previously stored here.....")


''' 7 show all students information  '''


def show():
    student_new = []
    if os.path.exists(filename):  # Check if the file exists
        with open(filename, 'r') as rfile:  # open the file
            student_old = rfile.readlines()  # read the file
        for list in student_old:
            student_new.append(eval(list))  # Save the found student information to the list
        if student_new:
            show_student(student_new)
    else:
        print("No information has been previously stored here.....")


# Display the student information stored in the list
def show_student(studentList):
    if not studentList:
        print("sorry! no data here!\n")
        return
    format_title = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    print(format_title.format("ID", "Name", "English score", "Chinese score", "Python score", "Total score"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get("id"), info.get("name"), str(info.get("english")), str(info.get("chinese")),
                                 str(info.get("python")),
                                 str(info.get("english") + info.get("chinese") + info.get("python")).center(12)))


if __name__ == "__main__":
    main()
