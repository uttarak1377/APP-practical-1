import re

file = open("emails.txt", "r")
text = file.read()
file.close()

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
emails = re.findall(pattern, text)
print(emails)
