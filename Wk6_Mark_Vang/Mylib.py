"""
Program Name: Mylib
Student Name: Mark Vang
Course: ENTD200 D001 Winter 2021
Instructor: Professor Nigatu
Date: 4/11/2021
Description: This is my updated library, I cleaned up a few unecessary comments. pointed a few functions 
to each other to make the code look cleaner.

Copy Wrong: This is my work.
"""

"""
This is a calculater that takes two ints and performs various fucntions.
"""
def add(x, y):
    return x + y
# Function line: subtracts two numbers
def subtract(x, y):
    return x-y
# Function line: multiplies two numbers
def multiply(x, y):
    return x * y
# Function line: divides two numbers
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Undefined"

class Basic:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def math(self, x, y): #My function to define the results of the calcuation and how to print it
    #math(x, y) initially had each math function on it's own, but I combined it in week 3.
        print("The result of ", x, "+", y, "=", add(x, y))
        print("The result of ", x, "-", y, "=", subtract(x, y))
        print("The result of ", x, "*", y, "=", multiply(x, y))
        try:   
            return print("The result of ", x, "/", y, "=", divide(x, y))
        except ZeroDivisionError: #Telling program, I know, thank you and print this in it's place.
            print("The result of ", x, "/", y, "=", divide(x, y))

class Verify:
    def __init__(self, x, y, high, low):
        self.x = x
        self.y = y
        self.high = high
        self.low = low
    
    def is_inrange(self, x, y, low, high): #Changed back after feedback.
        if low > x | y and high < x | y:
            print("The input values are outside the input ranges."
            "\nPlease check the numbers and try again"
            "\nThank you for using my calculator")
        
class Scalc:
    def __init__(self, stringa, stringb):
        self.stringa = stringa
        self.bstring = stringb
    
    def scalc(self, stringa, stringb): # This funciton does the math for my scalc. I did left my math(x,y) so it could compute the
    #rest of the code. I did not want to implement another 4 functions, so I added if - elif to calculate
    #the string.
        astring = ""
        bstring = ""

        astring = astring.split()
        bstring = bstring.split()
        num1 = int(float(astring[0])) #pull the number in the first spot
        num2 = int(float(astring[1])) #pull the number in the thrid spot
        Operator = (astring[2]) #pulls the operator in the second position
        if Operator == "+": #function was not used as, math() was used for the main calculation for the previous program
            print("The result is", add(num1, num2))
        elif Operator == "-":
            print("The result is", subtract(num1, num2))
        elif Operator == "*":
            print("The result is", multiply(num1, num2))
        elif Operator == "/":
            print("The result is", divide(num1, num2))

class Dict:
    res = ""

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def allInOne(self, n1, n2):
    #defining dict
        res = {"add": add(n1, n2), "sub": subtract(n1, n2), "mult": multiply(n1, n2), "div": divide(n1, n2)}
    
    #for loop for matching keys
        for key in res:
            if key == "add":
                print(n1, "+", n2, "=", add(n1, n2))
            if key == "sub":
                print(n1, "-", n2, "=", subtract(n1, n2))
            if key == "mult":
                print(n1, "*", n2, "=", multiply(n1, n2))
            if key == "div":
                print(n1, "/", n2, "=", divide(n1, n2))

    print(res)

def thankyou(): #Helps me recall this print if I need to use it multiple times.
    print("\nThank you for using my calculator!")