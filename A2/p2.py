import re

def sanitize_input(input_string):
    # Define disallowed characters
    disallowed_chars = r'[=!:@]'
    
    # Check for disallowed characters
    if re.search(disallowed_chars, input_string):
        raise ValueError("Input contains disallowed special characters.")

    return input_string

# Example usage
try:
    user_input = "Hello! World"
    sanitized_input = sanitize_input(user_input)
    print("Sanitized input:", sanitized_input)
except ValueError as e:
    print(e)
