import re

# Function to extract all email addresses from a given text
def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

# Function to validate a date in the format "YYYY-MM-DD"
def validate_date(date):
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(date_pattern, date):
        return True
    return False

# Function to replace all occurrences of a word with another word in a string
def replace_word(text, old_word, new_word):
    word_pattern = re.compile(rf'\b{old_word}\b', re.IGNORECASE)
    return word_pattern.sub(new_word, text)

# Example usage
text = """
Hello John, please send an email to john.doe@example.com. 
Also, contact jane_doe123@company.org for further assistance.
"""

print("Extracted Email Addresses:")
emails = extract_emails(text)
for email in emails:
    print(email)

date = "2025-04-05"
print("\nDate Validation:")
if validate_date(date):
    print(f"The date '{date}' is valid.")
else:
    print(f"The date '{date}' is not valid.")

string = "The quick brown fox jumps over the lazy dog. The fox is clever."
replaced_string = replace_word(string, "fox", "cat")
print("\nReplaced String:")
print(replaced_string)
