'''
py4e, Chapter 6, Exercise 1: Write a while loop that starts at the last
character in the string and works its way backwards to the first character in
the string, printing each letter on a separate line, except backwards.

William Kerley, 21.02.20
'''

fruit = 'banana'

index = len(fruit)-1            #set index to last letter of string
while index >= 0:               #print letters of words from last to first
    letter = fruit[index]
    print(letter)
    index = index - 1
