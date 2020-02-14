'''
py4e, Chapter 3, Exercise 7: Rewrite the grade program from the previous chapter
using a function called 'computegrade' that takes a score as its parameter and
returns a grade as a string.

    Score       Grade
    >= 0.9      A
    >= 0.8      B
    >= 0.7      C
    >= 0.6      D
    < 0.6       F

William Kerley, 14.02.20
'''

def commutegrade(sc):
    if 0.0 <=  sc <= 1.0:
        if sc >= 0.9:
            return "A"
        elif sc >= 0.8:
            return "B"
        elif sc >= 0.7:
            return "C"
        elif sc >= 0.6:
            return "D"
        else:
            return "F"
    else:
        return "Bad score"


score = input("Enter score: ")
try:
    score = float(score)
    grade = commutegrade(score)
    print(grade)
except:
    print('Bad score')
