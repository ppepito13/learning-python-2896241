# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#
import re

run = True
regex = re.compile('[^a-z]')

while run:
    teststr = regex.sub('', input("What should I check?").lower())
    compare_string = teststr[::-1]
    if teststr == "exit":
        break
    elif teststr == compare_string:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
