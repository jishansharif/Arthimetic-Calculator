#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:26:20 2019

@author: jishanmsharif
"""

# The function calculate takes in two numbers and an operator and returns the result.
# The operator is a string, the return type a number.
def calculate(a, b, operator):
    if operator == "+":
        return (a + b)
    elif operator == "-":
        return (a - b)
    elif operator == "*":
        return (a * b)
    elif operator == "/":
        return (a / b)

stack = []
while True:
    data = input("Enter number/operator: ")
    if (data == "+") or (data == "-") or (data == "*") or (data == "/"):
        # data is an operator, so we remove the last two values from the list
        # and perform the computation. The result is printed and saved for
        # future use.
        b = stack.pop()
        a = stack.pop()
        result = calculate(float(a), float(b), data)
        stack.append(result)
        print(result)
    else:
        # If data is not an operator, the value entered gets stored onto the
        # list for future use.
        stack.append(data)

