'''
py4e, Chapter 3, Exercise 2: Rewrite your pay program using 'try' and 'except'
so that your program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the program:

    Enter Hours: 20
    Enter Rate: nine
    Error, please enter numeric input

    Enter Hours: forty
    Error, please enter numeric input

William Kerley, 14.02.20
'''

hrs = input("Enter Hours: ")
try:
    hrs = float(hrs)
    rate = input("Enter Rate: ")
    try:
        rate = float(rate)
        if hrs <= 40:
            print("Pay:", hrs*rate)
        else:
            print("Pay:", 40*rate + (hrs-40)*rate*1.5)
    except:
        print("Error, please enter numeric input")
except:
    print("Error, please enter numeric input")
