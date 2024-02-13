'''Design a code which will find the given number is Palindrome number or not'''

def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

# Input from the user
user_input = int(input("Enter a number: "))

# Checking if the number is a palindrome
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome number.")
else:
    print(f"{user_input} is not a palindrome number.")
