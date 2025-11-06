# Student Manager GUI Program
# Made by: Stephanie :)

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk    # Import GUI dialog and message tools

FILENAME = "studentmarks.txt"   # File where student data will be stored

# =========== Core Functions ===========
def load_file(filename):
    students = []   # Initialize empty list to store student dictionaries
    try:
        with open(filename, "r") as f:
            f.readline()   # Skip the header line in the text file
            for line in f:
                code, name, m1, m2, m3, exam = [x.strip() for x in line.split(",")]  # Split each line by commas and remove any extra spaces
                marks = [int(m1), int(m2), int(m3), int(exam)]   
                students.append({"code": code, "name": name, "marks": marks})    # Append each student as a dictionary to the list
    except FileNotFoundError:
        messagebox.showwarning("Warning", f"{filename} not found. Starting with an empty list.")  # If the file is missing, show a warning and start with an empty list
    return students  # Return the list of students

def save_file(filename, students):
    with open(filename, "w") as f:  # Write all student records into the file (overwrite existing data)
        f.write("Code,Name,M1,M2,M3,Exam\n")  # Write the header line
        for s in students:
            f.write(f"{s['code']},{s['name']},{s['marks'][0]},{s['marks'][1]},{s['marks'][2]},{s['marks'][3]}\n")  # Write each student's data on a new line
    messagebox.showinfo("Saved", "Student records saved successfully!")  # Show confirmation message after saving

def calc(s):
    cw = sum(s["marks"][:3]) # Calculate coursework (sum of first three marks)
    exam = s["marks"][3]
    total = cw + exam
    percent = (total / 160) * 100
    grade = "A" if percent >= 70 else "B" if percent >= 60 else "C" if percent >= 50 else "D" if percent >= 40 else "F"  # Determine grade based on percentage range
    return cw, exam, total, percent, grade  # Return all calculated values

# =========== Display Functions ===========
def show_all():
    text.delete("1.0", tk.END) # Clear text box before displaying data
    if not students:
        text.insert(tk.END, "No student records found.")
        return
    total = 0    # Track total percentage for average calculation
    for s in students:
        cw, exam, t, p, g = calc(s)     # Get all computed results for each student
        text.insert(tk.END, f"{s['name']} ({s['code']})\n")
        text.insert(tk.END, f"Coursework: {cw}/60 | Exam: {exam}/100 | {p:.1f}% | Grade: {g}\n\n")
        total += p
    avg = total / len(students)     # Compute and display average percentage
    text.insert(tk.END, f"Total students: {len(students)} | Average: {avg:.2f}%")

def show_one():
    name = simpledialog.askstring("View Student", "Enter student name or code:")  # Prompt user to enter name or code
    if not name: return
    found = False
    text.delete("1.0", tk.END)
    for s in students:
        if s["code"] == name or s["name"].lower() == name.lower():  # Check for name or code match (case-insensitive for name)
            cw, exam, t, p, g = calc(s)
            text.insert(tk.END, f"{s['name']} ({s['code']})\n")
            text.insert(tk.END, f"Coursework: {cw}/60 | Exam: {exam}/100 | {p:.1f}% | Grade: {g}\n")
            found = True
    if not found:
        messagebox.showerror("Error", "Student not found!")

def show_highest():  # Display the student with the highest total marks
    if not students: return
    s = max(students, key=lambda s: calc(s)[2])
    text.delete("1.0", tk.END)
    cw, exam, t, p, g = calc(s)
    text.insert(tk.END, f"Top Student:\n{s['name']} ({s['code']})\nCoursework: {cw}/60 | Exam: {exam}/100 | {p:.1f}% | Grade: {g}")

def show_lowest():   # Display the student with the lowest total mark
    if not students: return
    s = min(students, key=lambda s: calc(s)[2])
    text.delete("1.0", tk.END)
    cw, exam, t, p, g = calc(s)
    text.insert(tk.END, f"Lowest Student:\n{s['name']} ({s['code']})\nCoursework: {cw}/60 | Exam: {exam}/100 | {p:.1f}% | Grade: {g}")

# =========== CRUD Operations ===========
def sort_students():    # Allow user to sort student list by total marks
    if not students:
        messagebox.showerror("Error", "No students to sort.")
        return
    order = simpledialog.askstring("Sort", "Enter order (asc/desc): ")  # Ask sorting order
    if order not in ["asc", "desc"]: return     # Ignore invalid input
    reverse = True if order == "desc" else False     # Set sorting direction
    students.sort(key=lambda s: calc(s)[2], reverse=reverse)    # Sort based on total marks
    show_all()

def add_student():
    code = simpledialog.askstring("Add Student", "Enter student code:")     # Prompt user for new student details
    name = simpledialog.askstring("Add Student", "Enter student name:")
    marks = []
    for i in range(1, 4):   # Collect three coursework marks
        mark = simpledialog.askinteger("Add Marks", f"Enter mark {i}:")
        marks.append(mark)
    exam = simpledialog.askinteger("Add Exam", "Enter exam mark:")
    marks.append(exam)
    students.append({"code": code, "name": name, "marks": marks})   # Add new student record to list
    messagebox.showinfo("Added", f"{name} added successfully.")
    show_all()  # Refresh display

def delete_student():   # Prompt for code or name of student to remove
    key = simpledialog.askstring("Delete", "Enter student code or name:")
    for s in students:
        if s["code"] == key or s["name"].lower() == key.lower():
            students.remove(s)  # Remove matching student
            messagebox.showinfo("Deleted", f"{s['name']} removed.")
            show_all()
            return
    messagebox.showerror("Error", "Student not found.")

def update_student():   # Allow user to modify name or marks of a student
    key = simpledialog.askstring("Update", "Enter student code or name:")
    for s in students:
        if s["code"] == key or s["name"].lower() == key.lower():
            choice = simpledialog.askstring("Update", "Update name or marks? (name/marks):")    # Ask what to update: name or marks
            if choice == "name":
                s["name"] = simpledialog.askstring("Update", "Enter new name:")     # Update name field
            elif choice == "marks":     # Update coursework and exam marks
                for i in range(3):
                    s["marks"][i] = simpledialog.askinteger("Update", f"Enter new mark {i+1}:")
                s["marks"][3] = simpledialog.askinteger("Update", "Enter new exam mark:")
            messagebox.showinfo("Updated", f"{s['name']}'s record updated.")
            show_all()
            return
    messagebox.showerror("Error", "Student not found.")

# =========== GUI Setup ===========
root = tk.Tk()  # Create main window
root.title("Student Manager (By Stephanie)")
root.geometry("950x500")

frame = tk.Frame(root)     # Create container frame for buttons
frame.pack(pady=10)        # Add some vertical spacing

students = load_file(FILENAME)      # Load student records from file at startup


# Define button labels and their associated functions
btns = [
    ("View All", show_all),
    ("View One", show_one),
    ("Highest", show_highest),
    ("Lowest", show_lowest),
    ("Sort", sort_students),
    ("Add", add_student),
    ("Delete", delete_student),
    ("Update", update_student),
    ("Save & Exit", lambda: [save_file(FILENAME, students), root.destroy()])
]

for (text_label, cmd) in btns:      # Create and display buttons horizontally
    tk.Button(frame, text=text_label, width=12, command=cmd).pack(side="left", padx=5)

text = tk.Text(root, wrap="word", width=80, height=25, bg="#f0f8ff")      # Create text area for displaying results
text.pack(pady=10)

root.mainloop()     # Run the GUI event loop

# =========== Student Marks Vid Link - https://youtu.be/3PMx8jUplSc ====================