import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^(Anya Taylor-Joy|John Cena|D'Angelo)$"
name_regex = re.compile(rf"{name}")
# matches = name_regex.fullmatch("D'Angelo")
# print(matches)


phone_number = r"\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4}"
phone_regex = re.compile(phone_number)
# matches=phone_regex.fullmatch("(555) 555-5555")
# print(matches)

email_address = r"^[a-z][a-z.\d]+@[a-z].+com$" 
email_regex = re.compile(email_address)
matches=email_regex.fullmatch("123john.cena@wwe.com")
print(matches)

