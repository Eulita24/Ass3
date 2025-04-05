def calculate_average(*args):
    try:
        if len(args) == 0:
            raise ValueError("No numbers provided. Please provide at least one number.")

        for num in args:
            if not isinstance(num, (int, float)):
                raise ValueError("All inputs must be numbers.")

        total = sum(args)
        count = len(args)
        return total / count
    except ValueError as e:
        print(f"Error: {e}")
        return None


# Prompt user to enter valid numbers
def prompt_for_numbers():
    while True:
        try:
            # Prompt user for input
            user_input = input("Enter numbers separated by spaces (e.g., 10 20 30): ")
            numbers = list(map(float, user_input.split()))
            return numbers
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            # Main program
            numbers = prompt_for_numbers()  # Get valid numbers from the user
            average = calculate_average(*numbers)  # Pass numbers using args
            if average is not None:
                print(f"The average of the numbers is: {average}")



