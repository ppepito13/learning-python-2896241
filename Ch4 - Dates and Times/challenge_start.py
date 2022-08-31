# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar


def count_days(y, m, d):
	cal = calendar.monthcalendar(y, m)
	days_no = 0
	for week in cal:
		if week[d] > 0:
			days_no = days_no + 1
	return days_no


run = True
try:
	while run:
		print("Which day of the week do you want to count?")
		print("0: Monday")
		print("1: Tuesday")
		print("2: Wednesday")
		print("3: Thursday")
		print("4: Friday")
		print("5: Saturday")
		print("6: Sunday")
		print("Or 'exit' to quit")
		day = input("? ")
		if day == "exit":
			run = False
			break
		elif int(day) > 6:
			raise ValueError
		else:
			given_day = int(day)

		given_year = int(input("Enter year: "))
		given_month = int(input("Enter month: "))

		day_count = count_days(given_year, given_month, given_day)
		print("There is", str(day_count), "day(s) in the month and year you've specified.")
		print("---------\n")

except Exception as e:
	print(e)
	print("Sorry, that's not valid input")
