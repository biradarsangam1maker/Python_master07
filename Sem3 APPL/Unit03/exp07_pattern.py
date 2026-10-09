import re
employee_data = "sangmeshwar 8208681730 biradarsangam9@gmail.com"
Email_pattern = r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+'
email = re.findall(Email_pattern, employee_data)
print("Email of Employee: ", email)
