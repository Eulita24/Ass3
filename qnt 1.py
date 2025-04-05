def classify_number(number):
    # Function to classify the number
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

def prompt_for_number():
    while True:
        try:
            # Prompt user for input
            user_input = input("Enter a valid integer: ")
            number = int(user_input)  # Try to convert to integer
            return number
        except ValueError:
            # Handle invalid input
            print("That's not a valid integer. Please try again.")

# Main program
while True:
    number = prompt_for_number()  # Prompt user until a valid integer is entered
    classification = classify_number(number)  # Classify the number
    print(f"The number {number} is {classification}.")
    break  # Break after successful classification (remove if you want a repeated loop)

