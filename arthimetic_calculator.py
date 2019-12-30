#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:26:20 2019

@author: jishanmsharif
"""

run ="x"
while run == "x":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    operator = input("Enter operator")
#Three variables assigned allowing users to input the first variable, second variable, and operator respectively
#The value entered is converted into a float 
    if operator == "+":
        print(first_number+second_number)
    elif operator == "-":
        print(first_number-second_number)
    elif operator == "*":
        print(first_number*second_number)
    elif operator == "/":
        print(first_number/second_number)
    else:
        print("Not a valid Operator")
#if conditions used enabling python to perform different tasks based on the input
    run = input("Continue using the calculator?")
#while loop is used to prevent the program from breaking down