# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
username0 = input("What is your name?\n")

if username0.upper() == "BOB":
  print("Welcome Bob!")
else:
  print("You are not Bob!")

# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
username1 = input("What is your name?\n")

if username1.upper() == "ALICE":
  print("Welcome Bob!")
else:
  print("You are not Alice!")

# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in".
#   If they get it wrong, print "Password failure".
password0 = input("Password?\n")

if password0 == "qwerty123":
  print("You have successfully logged in")
else:
  print("Password failure")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
question0 = int(input("Enter a random number\n"))
if question0 % 2 == 0:
  print("Even")
else:
  print("Odd")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
question1 = int(input("Please enter your first number\n"))
question2 = int(input("Please enter your second number\n"))
if question1 + question2 > 21:
  print("Bust")
else:
  print("Safe")

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
question3 = int(input("Please enter the length\n"))
question4 = int(input("Please enter the width\n"))
if question3 == question4:
  print(True)
else:
  print(False)

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years.
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
question3 = int(input("What is your annual salary?\n"))
question4 = int(input("How many years have you worked for the business?\n"))
if question4 > 3:
  print(float(question3 * .1))
else:
  print("No bonus")

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
question6 = int(input("Enter a whole number\n"))
if question6 > 0:
  print(question6**3)
else:
  print(question6 / 2)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob",
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".
question7 = str(input("What is your name?\n"))
if question7.upper() == "ALICE":
  print("Hello, Alice")
elif question7.upper() == "BOB":
  print("You're not Bob! I'm Bob")
else:
  print("You must be Charlie")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"
question8 = int(input("How old are you?\n"))
if question8 < 11:
  print("You're too young to go to this school")
elif question8 >= 11 and question8 <= 16:
  print("You can can come to this school")
elif question8 > 16:
  print("You're too old for school")
elif question8 == 0:
  print("You're not born yet!")

# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
question9 = str(input("What month is ?\n"))
if question9 == "March" or question9 == "April" or question9 == "May":
  print(question9 + " is in Spring")
elif question9 == "June" or question9 == "July" or question9 == "August":
  print(question9 + " is in Summer")
elif question9 == "September" or question9 == "October" or question9 == "Novemeber":
  print(question9 + " is in Autumn")
elif question9 == "December" or question9 == "January" or question9 == "February":
  print(question9 + " is in Winter")
else:
  print("I don't know")

# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
question10 = int(input("Enter your first number\n"))
question11 = int(input("Enter your second number\n"))
if question10 % 2 == 0 and question11 % 2 == 0:
  print("Even")
elif question10 % 2 != 0 and question11 % 2 != 0:
  print("Odd")
else:
  print(question10 * question11)

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
question12 = int(input("Enter your first number\n"))
question13 = int(input("Enter your second number\n"))
result0 = [question12, question13]
print(str(max(result0)) + " is the highest value")

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years,
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years.
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
question14 = int(input("What is your annual salary?\n"))
question15 = int(input("How many years have you worked for the business?\n"))
if question15 > 7:
  print(float(question14 * .2))
elif question15 > 5:
  print(float(question14 * .15))
elif question15 >= 3:
  print(float(question14 * .1))
else:
  print("No bonus")

# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest.
#   If all three ages are the same, print that.
question16a = str(input("Enter the first name\n"))
question16b = int(input("Enter their age\n"))
question17a = str(input("Enter the second name\n"))
question17b = int(input("Enter their age\n"))
question18a = str(input("Enter the third name\n"))
question18b = int(input("Enter their age\n"))
if question16b == question17b == question18b:
  print("They are all the same age")
elif question16b > question17b > question18b:
  print(question16a + " is the oldest at the age of " + str(question16b))
elif question17b > question18b:
  print(question17a + " is the oldest at the age of " + str(question17b))
else:
  print(question18a + " is the oldest at the age of " + str(question18b))

# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
question19a = str("First lesson")
question19b = int("Grade?")
question20a = str("Second lesson")
question20b = int("Grade?")
question21a = str("Second lesson")
question21b = int("Grade?")
