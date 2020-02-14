'''
py4e, Chapter 4, Exercise 6: Rewrite your pay computation with time-and-a-half
for overtime and create a function called 'computepay' which takes two
parameters ('hours' and 'rate').

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

William Kerley, 14.02.20
'''

def commutepay(hr,rt):
    if hr <= 40:
        return hr*rt
    else:
        return 40*rt + (hr-40)*rate*1.5

hours = input("Enter Hours: ")
try:
    hours = float(hours)
    rate = input("Enter Rate: ")
    try:
        rate = float(rate)
        pay = commutepay(hours,rate)
        print("Pay:", pay)
    except:
        print("Error, please enter numeric input")
except:
    print("Error, please enter numeric input")
