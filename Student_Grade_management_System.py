def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def student_main():
    name = input("Enter student name: ")
    m1 = int(input("Enter marks in Math: "))
    m2 = int(input("Enter marks in Science: "))
    m3 = int(input("Enter marks in English: "))

    avg = calculate_average(m1, m2, m3)
    grade = get_grade(avg)
    status = "Pass" if grade != "F" else "Fail"

    print("\n--- Report Card ---")
    print(f"Student Name: {name}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")

# Run the program
student_main()
