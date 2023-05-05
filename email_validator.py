#Email Validator Using Python Filter

import re

n = int(input())
valid_emails = []

# regex pattern for valid email addresses
pattern = r'^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'

for i in range(n):
    email = input().strip()
    if re.match(pattern, email):
        valid_emails.append(email)

valid_emails.sort()
print(valid_emails)