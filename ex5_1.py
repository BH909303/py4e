'''
py4e, Chapter 5, Exercise 1: Write a program which repeatedly reads numbers
until the user enters "done". Once "done" is entered, print out the total,
count, and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error message
and skip to the next number.

William Kerley, 21.02.20
'''

n = 0                           #intialize variables
count = 0
sum = 0

while True:
    n = input("Enter a number:")
    if n == 'done':
        break                   #exists loop if done

    try:
        n = float(n)            #checks for numeric input
        count = count + 1       #counter
        sum = sum + n           #sum
    except:
        print("Invalid input")

if count == 0:
    average = 0                 #prevent division by 0
else:
    average = sum/count         #find average

print(sum, count, average)
