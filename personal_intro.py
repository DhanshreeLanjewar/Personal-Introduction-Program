import pyinputplus as pyip

name = pyip.inputStr("What is your name? ")
age = pyip.inputInt("How old are you? ")
hobby = pyip.inputStr("What is your favorite hobby? ")
city = pyip.inputStr("Which city are you from? ")
college = pyip.inputStr("Which college are you studying in? ")

print()
print("Welcome", name)
print("Age:", age)
print("Hobby:", hobby)
print("City:", city)
print("College:", college)
