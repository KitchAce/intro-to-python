# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable.
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
x = float(2.2)
y = float(3.65)
z = float(x * y)
print("Rectangle of width " + str(x) + " and height " + str(y) + " has an area of " + str(z))

# 2. Write code that prints the length of the string, 'python'.
print(int(len("Python")))

# 3. Print out the first and third letter of the word 'python'.
name = "Python"
print(name[0])
print(name[2])

# 4. Ask the user to enter their name, and print out `Hello, <name>`.
username = input("What is your name?\n")
print("Hello " + username)


# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
userage = float(input("How old are you?\n"))
print("In 15 years you will be " + str(int(userage + 15)) + " years old")

# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old.
#   In 15 years time you will be <age_in_15_years_time>`.
nameprint = ("Hello " + username)
ageprint =  ("In 15 years you will be " + str(int(userage + 15)) + " years old")
print(nameprint + ", you are currently " + str(int(userage)) + " years old\n"+ ageprint)

# 7. Ask the user to enter their hometown, print it out in uppercase letters.
home = "manchester"
print(home.upper())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
usercolour = input("What is your favorate colour?\n")
print(len(usercolour))

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
usermonth = input("What is the current month?\n")
userweather = input("What is the wheather today?\n")
print("It is " + usermonth + " and it is " + userweather + " today.")

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string:
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
input0 = input("What month is it?\n")
input1 = int(input("What is temperature #1?\n"))
input2 = int(input("What is temperature #2?\n"))
input3 = int(input("What is temperature #3?\n"))
input4 = int(input("What is temperature #4?\n"))
input5 = int(input("What is temperature #5?\n"))
result0 = ("It is " + input0 + " and the average temperature is " + 
     str((input1+input2+input3+input4+input5)/5) + " degrees celsius")
print(result0)

# 11. Print out the above sentence but make the month upper case.
print(result0.upper())

# 12. Create a variable that holds your favourite animals and print it out.
#    Make sure the animals are all on different lines and tabbed.
animallist = ("\tWolf\n\tDog\n\tCat")
print(animallist)


# 13. Ask the user to enter their name as well as a number.
#    Print out the uppercase character at that position in the string.
username1 = input("What is your name?\n")
usernumber0 = int(input("What is your favorate number?\n")) - 1
print(username1[usernumber0])

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
string0 = "WelcometoPython"
print(string0[1:14])
