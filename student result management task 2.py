"""
Student Result Management System
---------------------------------
Bright Future Academy - stores student records, calculates grades
automatically, and generates class performance statistics.
"""

# Dictionary to hold all student records.
# Structure: { "Student Name": score (float) }
students = {}


def get_grade(score):
    """Return the letter grade for a given numeric score."""
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"


def get_valid_score():
    """Keep asking until the user enters a valid score between 0 and 100."""
    while True:
        raw = input("Enter score (0-100): ").strip()
        try:
            score = float(raw)
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if score < 0 or score > 100:
            print("Score must be between 0 and 100.\n")
            continue

        return score


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.\n")
        return

    if name in students:
        overwrite = input(f"{name} already exists. Overwrite score? (y/n): ").strip().lower()
        if overwrite != "y":
            print("No changes made.\n")
            return

    score = get_valid_score()
    students[name] = score
    print(f"Added {name} with score {score} (Grade: {get_grade(score)}).\n")


def view_students():
    if not students:
        print("No student records yet.\n")
        return

    print("\n{:<20}{:<10}{:<6}".format("Name", "Score", "Grade"))
    print("-" * 36)
    for name, score in students.items():
        print("{:<20}{:<10}{:<6}".format(name, score, get_grade(score)))
    print()


def update_score():
    name = input("Enter the name of the student to update: ").strip()

    if name not in students:
        print(f"No record found for '{name}'.\n")
        return

    print(f"Current score for {name}: {students[name]}")
    new_score = get_valid_score()
    students[name] = new_score
    print(f"Updated {name}'s score to {new_score} (Grade: {get_grade(new_score)}).\n")


def search_student():
    name = input("Enter the name of the student to search: ").strip()

    if name in students:
        score = students[name]
        print(f"\n{name} -> Score: {score}, Grade: {get_grade(score)}\n")
    else:
        print(f"No student named '{name}' was found.\n")


def class_statistics():
    if not students:
        print("No student records yet, so no statistics to show.\n")
        return

    scores = list(students.values())
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)

    highest_students = [n for n, s in students.items() if s == highest]
    lowest_students = [n for n, s in students.items() if s == lowest]

    print("\n--- Class Statistics ---")
    print(f"{'Total students':<15}: {len(students)}")
    print(f"{'Highest score':<15}: {highest} ({', '.join(highest_students)})")
    print(f"{'Lowest score':<15}: {lowest} ({', '.join(lowest_students)})")
    print(f"{'Average score':<15}: {average:.2f}\n")


def show_menu():
    print("===== Student Result Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Score")
    print("4. Search Student")
    print("5. Class Statistics")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_score()
        elif choice == "4":
            search_student()
        elif choice == "5":
            class_statistics()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")


if __name__ == "__main__":
    main()
