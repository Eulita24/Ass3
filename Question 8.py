import random

def generate_random_numbers(count, start, end):
    """Generate a list of random integers."""
    return [random.randint(start, end) for _ in range(count)]

def calculate_average(numbers):
    """Calculate and return the average of a list of numbers."""
    if len(numbers) == 0:
        return 0  # Avoid division by zero
    return sum(numbers) / len(numbers)

# Main Program
random_numbers = generate_random_numbers(10, 1, 100)  # Generate 10 random integers between 1 and 100
average = calculate_average(random_numbers)  # Calculate their average

print("Random Numbers:", random_numbers)
print("Average:", average)
