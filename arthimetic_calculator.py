#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:26:20 2019

@author: jishanmsharif
"""
    
def calculate(num1,num2,operator):
    if operator == "+":
        return (num1 + num2)
    elif operator == "-":
        return (num1 - num2)
    elif operator == "*":
        return (num1 * num2)
    elif operator == "/":
        return (num1 / num2)
    else:
        return None
    
first_number = float(input(""))    
run ="x"
while run == "x":
    user_input=input("")
    if user_input == "q":
        break
    second_number = float(user_input)
    operator = input("")
    first_number = calculate(first_number,second_number,operator)
    print(first_number)

    
