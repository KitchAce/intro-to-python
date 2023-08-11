# Session 5 Exercises
import random
## Section A
# 1. Print 10 random numbers.
for x in range(10):
  print(random.randint(1, 10))

# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .
number = 0
while number != 7:
  number = int(input("Enter a number!\n"))
print("Wow lucky number 7!")

#number = 0
#while number != random.randint(1,10):
#  number = int(input("Enter a number!\n"))

#print("You guessed the random number!")

# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.python
w = int(input("What is the width? (CM)"))
h = int(input("What is the hight? (CM)"))
print((w * h) / 100)

# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".
guess = 0
password = input("Enter pasword\n")
while guess <2:
  if password == "qwerty123":
    print("Correct password")
    break
  else:
    password = input("Password incorrect, try again\n")
    guess += 1

if guess == 2:
  "Password failure"


# 5. Add up all the numbers from 1 to 500 and print the answer.
answer = 0
for nx in range(1,501):
    answer += nx

print(answer)


# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
list1 = []
inputcount = 0

while inputcount < 10:
  list1.append(input("Enter a random number.\n"))
  inputcount += 1
  
while listx < len(list1):
  if listx == 99:
    print(listx)
  listx += 1

# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36



# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.



# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.



# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name



# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games
