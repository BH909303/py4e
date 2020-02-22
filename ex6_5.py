'''
py4e, Chapter 6, Exercise 5: Take the following Python code that stores a
string:

str = 'X-DSPAM-Confidence: 0.8475 '

Use find and string slicing to extract the portion of the string after the colon
character and then use the float function to convert the extracted string into a
floating point number.

William Kerley, 22.02.20
'''

str = 'X-DSPAM-Confidence: 0.8475 '

cp = str.find(':')          #Finds poistion of colon
n = str[c+1:]               #slices string after the colon
f = float(n)                #converts number to floating point
print(f)
