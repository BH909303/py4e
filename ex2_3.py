"""
P4YE, Chapter 2, Exercise 3: Write a program to prompt the user for hours and
rate per hour to compute gross pay.

William Kerley, 10.02.20
"""

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

hrs = float(hrs)
rate = float(rate)

print("Pay: ", hrs*rate)
