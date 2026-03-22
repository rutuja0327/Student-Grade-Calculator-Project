# Function to calculate grade and message
def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent! Keep shining! 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good job! You can do even better! 😊"
    elif 60 <= marks <= 69:
        return "D", "Keep trying! Improvement is key! 💪"
    else:
        return "F", "Don't give up! Work harder next time! 📚"


# Function to get valid marks input
def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a valid number.")


# Main program
def main():
    name = input("Enter student name: ")
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", name.upper() + ":")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


# Run the program
if __name__ == "__main__":
    main()
