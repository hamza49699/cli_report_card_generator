def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

students = []  # List to store student records

while True:
    print("\n📌 Enter Student Details")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    try:
        math = int(input("Math marks: "))
        physics = int(input("Physics marks: "))
        urdu = int(input("Urdu marks: "))
        english = int(input("English marks: "))
        computer = int(input("Computer marks: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        continue

    total = math + physics + urdu + english + computer
    percentage = total / 500 * 100
    grade = calculate_grade(percentage)

    # Store student data in a list
    students.append({
        "Name": name,
        "Roll Number": roll,
        "Math": math,
        "Physics": physics,
        "Urdu": urdu,
        "English": english,
        "Computer": computer,
        "Total Marks": total,
        "Percentage": f"{percentage:.2f}%",
        "Grade": grade
    })

    print(f"\n✅ Record of {name} inserted successfully.")
    
    more = input("\nDo you want to insert more? (Y/N): ").strip().lower()
    if more != 'y':
        break

# Display all report cards after data entry
print("\n📜 --- All Student Report Cards ---")
for student in students:
    print("\n" + "-" * 40)
    print(f"🎓 Student: {student['Name']}  |  Roll No: {student['Roll Number']}")
    print("-" * 40)
    print(f"📚 Math Marks: {student['Math']}")
    print(f"📚 Physics Marks: {student['Physics']}")
    print(f"📚 Urdu Marks: {student['Urdu']}")
    print(f"📚 English Marks: {student['English']}")
    print(f"📚 Computer Marks: {student['Computer']}")
    print(f"📊 Total Marks: {student['Total Marks']} / 500")
    print(f"📈 Percentage: {student['Percentage']}")
    print(f"🏆 Grade: {student['Grade']}")
print("\n✅ Report Generation Complete!")
