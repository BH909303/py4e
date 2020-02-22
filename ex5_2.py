'''
py4e, Chapter 5, Exercise 2: Write another program that prompts for a list of
numbers as above and at the end prints out both the maximum and minimum of the
numbers instead of the average.

William Kerley, 21.02.20
'''


n = 0                           #intialize variables
sum = 0
count = 0
max = 0
min = 0

while True:
    n = input("Enter a number: ")
    if n == 'done':
        break                   #exists loop if done

    try:
        n = float(n)            #checks for numeric input
        if count == 0:          #defines min and max for first entry
            max = n
            min = n
        count = count + 1       #counter
        sum = sum + n           #sum
        if n > max:
            max = n             #check for maximum
        if n < min:
            min = n             #check for minimum
    except:
        print("Invalid input")

print(sum, count, max, min)
