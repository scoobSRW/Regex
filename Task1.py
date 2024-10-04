import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
exclude_domain = "exclude.com"

# Regex to extract all email addresses except those from exclude_domain
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!{})[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b".format(re.escape(exclude_domain)), text)

print(emails)