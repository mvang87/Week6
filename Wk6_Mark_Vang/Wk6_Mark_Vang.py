"""
Program Name: Wk6_Mark_Vang
Student Name: Mark Vang
Course:ENTD220 D001 Winter 2021
Instructor: Professor Nigatu
Date: 4/11/2021
Description: 

I cleaned this up from last week, I removed a few thing thing from is_inrange as I was overloading
it. Changed from 10 x 10 to 10 10 x because of assignment requirements.

This is a simple code, it calculates numbers from the users input, it also test to make sure those numbers
are within range as defined by the user.

It also takes a strings and calculates it.

It also takes a menu input and calculates from there. Scalc was giving me issues, so I just nestled another scalc
in this weeks assignment.

From the second string, bstring, it now stores that information into a dictionary list.

Copy Wrong: This is my work.
"""
# from Mylib import *
import Mylib

try:
    calculate = input("Would you like to use the calculator? Yes or No: ")
    calculate = calculate.lower()
except KeyboardInterrupt:
    print("You have manually terminated the program.")
    exit(0) #exit(0) is needed otherwise it will process and go down to the else block below

"""
Keyboard Interupput was added here since I am requiring an input to here to begin the calculation.
It tells the user, that they have manually exitted the program.

The Keyboard Interrupt was also added below in the loop. This would catch the error if the user 
exited manually anytime during the loop with ctrl-c.
"""
menu = ["1. Add two numbers", "2. Subtract two numbers", "3. Multiply two numbers", 
        "4. Divide two numbers", "5. Scalc", "6. All In One"]
try: 
    while calculate == "yes":  
        #Basic inputs
        low = int(float(input("Please enter your Lower range: "))) #float was added for non whole numbers
        high = int(float(input("Please enter your Higher range: ")))
        x = int(float(input("Please enter your first number: ")))
        y = int(float(input("Please enter your second number: ")))

        #String Input
        stringa = input("Please a math equation you would like solved as (10 10 +): ") #Changed back after feedback

        #Menu Input
        for s in menu:
            print(s)
        selection = input("Please select an operation from the menu: ")

        #Input for n1 and n2
        stringb = input("Please enter two numbers to calculate and an operator for Scalc: ")
        
        #Prints out results
        print(Basic.math())
        print(scalc())
        print(thankyou)

        #Loop
        calculate = input("Would you like to calculate again? Yes or No: ")
        calculate = calculate.lower()
    #if statement was added, so that variations of no could be caught
    if calculate == "no": 
        print("Have a great day!")
    else:
        print("Please enter only Yes or No. Have a great day!")
        #Please enter only yes or no added to help the user understand other inputs were not accepted
except KeyboardInterrupt:
    print("You have manually terminated the program.")
    exit(0)