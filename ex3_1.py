'''
py4e, Chapter 3, Exercise 1: Rewrite your pay computation to give the employee
1.5 times the hourly rate for hours worked above 40 hours

    Enter Hours: 45
    Enter Rate: 10
    Pay: 475.0

William Kerley, 14.02.20
'''

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

hrs = float(hrs)
rate = float(rate)

if hrs <= 40:
    print("Pay:", hrs*rate)
else:
    print("Pay:", 40*rate + (hrs-40)*rate*1.5)
