import re

def password_strength(password):
    if len(password)<8:
        return "Weak: Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password): # WE USE NOT IF ANY(CONDITION) AGAR DIGIT NHI HAI TOH CONDITION FALSE HOGI MAGAR NOT IUSAI TRUE KARDEGA JISSAI RETURN WORK KARAGA
        return "Weak: Password must contain at least one digit."
    if not any(char.isalpha() for char in password):
        return "Weak: Password must contain at least one letter."
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        '''
• re.search() looks for any character that matches the pattern in the brackets [...].
• This is a raw string (indicated by r'') to avoid escaping issues.
• Matches any special character listed between the brackets.
        '''
        return "Medium: Password must contain at least one special character."
    
    # If all conditions are met, the password is considered strong.
    return "Strong: Password meets all criteria."
'''
✅ So if none of those if conditions trigger, that means:
	•	Length is OK ✅
	•	Contains digits ✅
	•	Contains letters ✅
	•	Has uppercase ✅
	•	Has lowercase ✅
	•	Has a special character ✅

Then we finally reach the last line:
'''

def password_checker():
    print("Welcome to the Password Strength Checker!")
    while True:
        password = input("Enter a password to check its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Exiting the Password Strength Checker. Goodbye!")
            break
        strength = password_strength(password)
        print(strength)    

if __name__ == "__main__":
    password_checker()