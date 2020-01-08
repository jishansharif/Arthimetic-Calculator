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

while True:
    user_input=input("")
    if user_input == "q":
        break
    second_number = float(user_input)
    operator = input("")
    first_number = calculate(first_number,second_number,operator)
    print(first_number)


# take a list
#Create two variables based on the last elements
# Perform operation on those two variables
#LOOP!
    
#def calculate(num1,num2,operator):
    #if operator == "+":
        #return (num1 + num2)
    #elif operator == "-":
     #   return (num1 - num2)
   # elif operator == "*":
   #     return (num1 * num2)
  #  elif operator == "/":
   #     return (num1 / num2)
  #  else:
     #   return None
    
#first_number = input([])   

#while True:
  #  user_input=first_number.pop(-1)
    #if user_input == "q":
        #break
    #second_number = first_number.pop(-2)
    # first_number = calculate(first_number,second_number,operator)
   # print(first_number)
while True:  
    initial_step = (input("Enter list here "))
    variable_one = initial_step.pop(-1)
    variable_two = initial_step.pop(-2)

    new_operator = float(input("Enter Operator"))
    if new_operator == "+":
        print (variable_one + variable_two)
    elif new_operator == "-":
        print (variable_one - variable_two) 
    elif new_operator == "*":
        print (variable_one * variable_two)
    elif new_operator == "/":
        print(variable_one / variable_two)
    else:
        print("Nothing")
    

