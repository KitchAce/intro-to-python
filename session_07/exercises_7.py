# Session 7 Exercises


shirt = { "size": "Large", 
             "colour": "Red" }
#del(shirt["size"])

print(shirt)

## Section A
# 1. Write a function that prints your name
def myname():
  print("My name is Marc")
  
myname()


# 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".
def yourname(name):
  print("Hello, " + name)

yourname("Bob")

# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.
names = ["Alice", "Bob", "Charlie"]
for people in names:
  yourname(people)

# 4. Write a function that prints the area of two passed in parameters.
def area(w, h):
  print("Area is " + str(w * h))

area(10, 25)


# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.
def print_list(list):
  for item in list:
    print(item)

print_list(["Item 1", "Item 2", "Item 3"])


# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".
def age(age):
  if age <= 0:
    print("You're not born yet!")
  elif age < 11:
    print("You're too young to go to this school")
  elif age >= 11 and age <= 16:
    print("You can can come to this school")
  elif age > 16:
    print("You're too old for school")
  else:
    print("You did not answer")

age(int(input("How old are you?\n")))

# <---------------------------------------------------------------------------------------------->


## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).
def is_odd(num):
  if num % 2 == 1:
    return True
  else:
    return False

print(is_odd(1))
print(is_odd(10))


# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.
def wordback(word):
  return word[::-1]

print(wordback("hello"))

# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```
def stars(num):
  star = ""
  for x in range(-1 , num):
    star = star + "*"
  print(star)
  if num > 1:
    stars(x-1)

stars(10)

# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".
x = 0
def padlock(userx):
  if userx == 1234:
    print("Unlocked")
  else:
    print("Locked")

padlock(2313)
padlock(1234)

# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
def limit(limit):
  sumx = 0
  for i in range(0,limit + 1):
    if i % 3 == 0:
      sumx += i
    elif i % 5 == 0:
      sumx += i
  return(sumx)

print(limit(20))

# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.
def is_prime(px):
  primeans = False
  if px % px == 1:
    primeans == True
    
#return(is_prime(7))

  

# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.

# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not.
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.
