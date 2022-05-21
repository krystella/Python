# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:06:31 2022

@author: Krystella

Course: Scientific Computing with Python - Prof. Charles Severance

Title: Exercises - Conditional Code

"""

# Q.3 Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours

hrs = input('How many hours have you worked? ')
rate = input('What is your hourly rate? ')
if float(hrs) <= 40:
    pay = float(hrs) * float(rate)
else :
    pay = (40 * float(rate)) + (((float(hrs)) - 40) * (float(rate)) * 1.5)
print('Your gross pay is: ', pay)


# Q.4 