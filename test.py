import re

regex = '\d{8,8}'
email = "1236w719"
if (re.search(regex, email)):
    print("Valid Email")

else:
    print("Invalid Email")