# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(fruits)

# 2. Add "Grapes" to the list and print the list.
fruits.append("Grape")
print(fruits)

# 3. Change "Pears" to "Strawberries" and print the list.
fruits[2] = "Strawberries"
print(fruits)

# 4. Remove "Apples" from the list and print the list.
del (fruits[0])
print(fruits)

# 5. Print out the current length of the list.
print(len(fruits))

# 6. Order the list alphabetically.
fruits.sort()

# 7. Print out the list again.
print(fruits)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
for myfruit in fruits:
  print(myfruit)

# 2. Print the numbers 1 to 100 (including the number 100).
for range1 in range(1, 101):
  print(range1)

# 3. Print all odd numbers from 1 to 100.
for range2 in range(1, 101, 2):
  print(range2)

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
notheld = [1916, 1940, 1944, 2020]
for olyyears in range(1896, 2020, 4):
  if olyyears not in notheld:
    print(olyyears)

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
randnum = [2, 3, 5, 75, 12, 623, 63, 12, 54, 99]
for range4 in randnum:
  if range4 % 2 == 0:
    print(range4)

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
namelist = ["Bob", "Marc", "Alex", "Jim", "John"]
for range5 in namelist:
  print("Hello " + str(range5))

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
word = "supercalifragilisticexpialidocious"
indexword = range(0, 34)
for range6 in indexword:
  print(word[range6])

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz".
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
