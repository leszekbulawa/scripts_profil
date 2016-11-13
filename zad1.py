import time
import calendar

def name_input(prompt):
	while True:
		try:
			value = input(prompt)
		except:
			print("Sorry, try again.")
			continue
		if not value.isalpha():
			print("Sorry, try again.")
		else:
			break
	return value

def age_input(prompt):
	while True:
		try:
			value = int(input(prompt))
		except:
			print("Sorry, try again.")
			continue
		if value < 0:
			print("Sorry, your response must not be negative.")
			continue
		else:
			break
	return value

def h_year(age):
	return int(time.strftime('%Y')) + 100 - age

name = name_input('Please, enter your first name: ')
sname = name_input('Please, enter your last name: ')
age = int(age_input('Please, enter your age: '))

if calendar.isleap(h_year(age)):
	leap = 'is'
else:
	leap = 'is not'

print('Hello', name+'.', 'You will reach hundred years old in', h_year(age), 'and it', leap, 'a leap-year.')
