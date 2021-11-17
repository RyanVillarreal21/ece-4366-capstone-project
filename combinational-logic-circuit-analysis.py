import math as mt
import string as st
import re

def checkExpress(expr):
    n = len(expr)
    i = 0
    #print(n)
    for i in range(0, n - 2, 2):
        if(expr[i + 1] == 'A'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'B'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'C'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'D'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'E'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'F'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'G'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'H'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'I'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'J'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'K'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'L'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'M'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'N'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'O'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'P'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'Q'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'R'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'S'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'T'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'U'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'V'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'W'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'X'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'Y'):
            i = i + 1
            continue
        elif(expr[i + 1] == 'Z'):
            i = i + 1
            continue
        elif(expr[i + 1] == '+'):
            i = i + 1
            continue
        elif(expr[i + 1] == "'"):
            i = i + 1
            continue
        elif(expr[i + 1] == "("):
            i = i + 1
            continue
        elif(expr[i + 1] == ")"):
            i = i + 1
            continue
        else:
            if(expr[i + 1] != ''):
                expr = input("Invalid boolean expression. Please enter another: ")
                checkExpress(expr)
            else:
                print("Evaluation success")
                break
    # match = re.findall(r"[A-Z]", expr)
    # if match:
    #     return expr
    # else:
    #     expr = input("Invalid boolean expression. Please enter another: ")
    #   checkExpress(expr)

def evaluate(arr, x, y):
    # stack = []
    # n = len(arr)
    # l = x
    # j = y
    # orGat = 0
    # andGat = 0
    # notGat = 0

    # while(l < n):
    #     if(arr[l] == "("):
    #         while(arr[l] == "(" & arr[j] != ")"):
    #             if(arr[j] == "+"):
    #                 ordGat = ordGat + 1
    #                 j = j + 1
    #                 continue
    #             elif(arr[j] == "'"):
    #                 notGat = notGat + 1
    #                 j = j + 1
    #                 continue
    #             elif(arr[j] == ")"):
    #                 return evaluate(arr, l, j)
    #             else:
    #                 andGat = andGat + 1
    #                 j = j + 1

    #     elif(arr[l] == "+"):
    #         orGat = orGat + 1
    #         l = l + 1
    #         continue
    #     elif(arr[l] == "'"):
    #         notGat = notGat + 1
    #         l = l + 1
    #     else:
    #         andGat = andGat + 1
    #         l = l + 1
    #         continue

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+':1, '*':1, "'":2}
     
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
     
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
     
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
     
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()
 
    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except KeyError:
            return False
             
    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):
         
        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)
             
            # If the character is an '(', push it to stack
            elif i  == '(':
                self.push(i)
 
            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while( (not self.isEmpty()) and
                                self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
 
            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
 
        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
 
        print (self.output)

expr = input("Enter a boolean expression: ")
checkExpress(expr)
#arr = str.split(expr)
evaluate(expr)
#print(expr)