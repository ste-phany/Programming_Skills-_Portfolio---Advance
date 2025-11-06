# Student Manager Python Program 
# Made by: Stephanie :)

def load_file(filename): # Load student data from the text file
    students = [] # Student record in (list)
    with open(filename, "r") as f:
        f.readline()  # Skips the header line 
        for line in f:
            code, name, m1, m2, m3, exam = [x.strip() for x in line.split(",")] # Split each line by commas & remove whitespace
            marks = [int(m1), int(m2), int(m3), int(exam)] # Converts marks to integers
            students.append({"code": code, "name": name, "marks": marks}) # How it will be layouted when pushed to the dictonary list
    return students        # Return the list of student dictionaries

def save_file(filename, students):  # Save students back to file
    with open(filename, "w") as f:
        f.write("Code,Name,M1,M2,M3,Exam\n")  # Header
        for s in students:
            f.write(f"{s['code']},{s['name']},{s['marks'][0]},{s['marks'][1]},{s['marks'][2]},{s['marks'][3]}\n")

def calc(s):                       # This function calculates coursework, exam, total, perentage & grade
    cw = sum(s["marks"][:3])       # Sum of the first 3 marks
    exam = s["marks"][3]           # Exam Mark
    total = cw + exam              # Total Mark
    percent = (total / 160) * 100  # Percentage out of 160
    grade = "A" if percent >= 70 else "B" if percent >= 60 else "C" if percent >= 50 else "D" if percent >= 40 else "F"   # Assign grade based on percentage
    return cw, exam, total, percent, grade

def show(s): # This function display every single student's information
    cw, exam, t, p, g = calc(s) # Get Calculations
    print(f"\n{s['name']} ({s['code']})")
    print(f"Coursework: {cw}/60 | Exam: {exam}/100 | {p:.1f}% | Grade: {g}")

def show_all(students): # This displays all the students information and overall average
    total = 0  # Variable to sum percentage
    for s in students:
        show(s)
        total += calc(s)[3]  # Add student' percentage to total
    print(f"\nTotal students: {len(students)} | Average: {total/len(students):.2f}%")

def sort_students(students):   # Function to sort student records based on total marks
    if not students:           # Check if the student list is empty
        print("No students to sort.")
        return                 # Exit if there are no records to sort
    order = input("Sort by Total marks (asc/desc): ").lower()     # Ask the user whether to sort in ascending or descending order
    reverse = True if order == "desc" else False                  # If the user enters 'desc', reverse sorting will be enabled (highest to lowest)
    # Sort students using the total marks calculated by calc(s)[2]
    # Assuming calc(s) returns (avg, grade, total) — hence [2] is total marks
    students.sort(key=lambda s: calc(s)[2], reverse=reverse)
    # Display all sorted students using show_all()
    show_all(students)

def add_student(students):  # Function to add a new student record
    code = input("Enter student code: ")    # Collect student information from user input
    name = input("Enter student name: ")
    marks = []               # Initialize an empty list for storing marks
    for i in range(1, 4):    # Collect 3 subject marks from the user
        marks.append(int(input(f"Enter mark {i}: ")))
    exam = int(input("Enter exam mark: "))        # Collect exam mark separately and append it to the marks list
    marks.append(exam)
    students.append({"code": code, "name": name, "marks": marks})     # Add a new student dictionary to the students list
    print(f"{name} added successfully.")    # Confirmation message

def find_student(students):  # Helper function to locate a student by code or name
    key = input("Enter student code or name: ").strip()     # Get search input and remove extra spaces
    for s in students:       # Iterate through all student records
        if s["code"] == key or s["name"].lower() == key.lower():      # Match either by exact student code or by name (case-insensitive)
            return s         # Return the matched student record
    print("Student not found.")     # If no student found, notify user
    return None              # Return None if search fails

def delete_student(students):   # Function to delete an existing student record
    s = find_student(students)  # Find the student using the helper function
    if s:    # If student exists
        students.remove(s)
        print(f"{s['name']} has been deleted.")    # Confirmation message

def update_student(students):  # Function to update student details (name or marks)
    s = find_student(students)  # Search for the student to update
    if not s:    # If not found, exit the function
        return
    print("\nWhat do you want to update?")     # Display update options
    print("1. Name  2. Marks  3. Cancel")
    choice = input("Choose: ")
    if choice == "1":    # If user chooses to update the name
        s["name"] = input("Enter new name: ")
    elif choice == "2":   # If user chooses to update the marks
        for i in range(3):  # Update 3 subject marks
            s["marks"][i] = int(input(f"Enter new mark {i+1}: "))
        s["marks"][3] = int(input("Enter new exam mark: "))
    print(f"{s['name']}'s record updated.")  # Display success message after update

def main():  # The mai function to control the program flow
    filename = "studentmarks.txt"   # The file containing student data
    students = load_file(filename)  # Load students from file

    while True: # Main menu loop
        print("\n1.View All  2.View One  3.Highest  4.Lowest  5.Exit")
        ch = input("Choose: ")
        if ch == "1": show_all(students)
        elif ch == "2":
            for i, s in enumerate(students, 1): print(f"{i}. {s['name']}")
            n = int(input("Pick: ")) - 1
            if 0 <= n < len(students): show(students[n])
        elif ch == "3": show(max(students, key=lambda s: calc(s)[2]))
        elif ch == "4": show(min(students, key=lambda s: calc(s)[2]))
        elif ch == "5": sort_students(students)
        elif ch == "6": add_student(students)
        elif ch == "7": delete_student(students)
        elif ch == "8": update_student(students)
        elif ch == "9":
            save_file(filename, students)    
            break # Exit the Program
        else: print("Invalid choice.") # Handles the invalid input
 
if __name__ == "__main__":
    main() # Calls the main loop
