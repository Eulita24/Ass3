def get_valid_number():
    while True:
        try:
            # Prompt user for input
            user_input = input("Enter a valid number: ")
            number = float(user_input)  # Convert input to a number (integer or float)
            return number
        except ValueError:
            # Handle invalid input
            print("That's not a valid number. Please try again.")

# Main program
number = get_valid_number()  # Get a valid number from the user
print(f"You have successfully entered the number: {number}")
