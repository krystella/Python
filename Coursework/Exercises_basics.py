# -*- coding: utf-8 -*-
"""
Created on Sat May 21 08:19:24 2022

@author: Krystella

Course: Scientific Computing with Python - Prof. Charles Severance

Title: Exercises - Introduction

"""

# Q.1 Write a program that uses a print statement to say 'hello world

print("Hello world")


# Q.2 Write a program that uses 'input' to prompt a user for their name and the welcomes them

username = input('Enter your name: ')
print("Hello,", username)

    # 'input' and 'print' used as functions
    

# Q.3 Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = input('How many hours have you worked? ')
rate = input('What is your hourly rate? ')
pay = float(hours) * float(rate)
    # float converts the string into a floating number that allows for computation
print("Your gross pay is: ", pay)


