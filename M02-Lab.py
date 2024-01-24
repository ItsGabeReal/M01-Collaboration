# Name: Gabriel Wilson
# Filename: M02-Lab.py
# Description: Accepts a student's last name, first name, and gpa, then prints if the student has made the Honor Roll or Dean's List.

while True:
    lastName = input("enter last name (or ZZZ to quit): ")

    if lastName == 'ZZZ':
        break

    firstName = input("enter first name: ")

    # This loop runs until a valid gpa is entered
    while True:
        gpaInput = input("enter " + firstName + " " + lastName + "'s gpa: ")

        # Try to convert gpa string to a float. If it fails, then print a message
        try:
            gpa = float(gpaInput)
        except:
            print("that is not a valid gpa. it must be a number.")
            continue

        # Check if the gpa is within the valid range
        if gpa >= 0 and gpa <= 4:
            break
        else:
            print("that is not a valid gpa. it must be between 0 and 4.")

    if gpa >= 3.5:
        print("this student has made the Dean's List!")
    elif gpa >= 3.25:
        print("this student has made the Honor Roll!")
