# Custom Exception Class
class NegativeNumberError(Exception):
    def __init__(self, message="Number is negative"):
        super().__init__(message)

# Function to check if the number is positive
def check_positive(number):
    if number < 0:
        raise NegativeNumberError(f"Error: {number} is negative.")

# Demonstration using a try block
try:
    user_input = int(input("Enter a number: "))  # Prompt user for input
    check_positive(user_input)  # Check if the number is positive
    print(f"{user_input} is positive!")
except NegativeNumberError as e:
    print(e)  # Print the error message if exception occurs
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
