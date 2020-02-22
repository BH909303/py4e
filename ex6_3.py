'''
py4e, Chapter 6, Exercise 3: Encapsulate this code in a function named count,
and generalize it so that it accepts the string and the letter as arguments.

William Kerley, 21.02.20
'''

#function counting the number of a specified letter in a word
def count(word, letter):
    sum = 0
    for letter in word:
        if letter == 'a':
            sum = sum + 1
    print(sum)

count('banana', 'a')
