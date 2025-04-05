# List of names
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

# Write names to a file
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")  # Write each name on a new line

# Read names from the file and print to console
with open("names.txt", "r") as file:
    print("Names from the file:")
    for line in file:
        print(line.strip())  # Strip to remove extra newlines or spaces
