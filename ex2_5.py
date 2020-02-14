"""
py4e, Chapter 2 Exercise 5: Write a program which prompts the user for a Celsius
temperature,convert the temperature to Fahrenheit, and print out the converted
temperature.

William Kerley, 10.02.20
"""

cel = input("Temperature in Celcius: ")
cel = float(cel)

print("Temperature in Fahrenheit:", (cel * 1.8) + 32 )
