import re

def passval(password):
	pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
	check = pattern.fullmatch(password)
	if check:
		return "It's a valid password"
	else:
		return "It's an invalid password"


password = input("Enter password: ")
print(passval(password))







