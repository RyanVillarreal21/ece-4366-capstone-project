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
            # else:
            #     print("Evaluation success")
            #     break
    return expr
#     match = re.findall(r"[A-Z]", expr)
#     if match:
#         return expr
#     else:
#         expr = input("Invalid boolean expression. Please enter another: ")
#         checkExpress(expr)

#def evaluate(arr, x, y):
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

def andSym(expr):
    n = len(expr)
    i = 0
    for i in range(0, n - 2, 2):
        if(expr[i + 1] == "+" or "'" or "(" or ")"):
            i += 1
            continue
        else:
            expr = expr[:i] + "*" + expr[i:]
            i += 1
            continue
    return expr

OPERATORS = set(['+', '*', "'", '(', ')'])  # set of operators
PRIORITY = {'+':1, '*':2,"'":3} # dictionary having priorities 

def infix_to_postfix(expr): #input expression
    stack = [] # initially stack empty
    output = '' # initially output empty

    for ch in expr:
        if(ch not in OPERATORS):  # if an operand then put it directly in postfix expression
            output+= ch
        elif(ch == '('):  # else operators should be put in stack
            stack.append('(')
        elif(ch == ')'):
            while(stack and stack[-1] != '('):
                output += stack.pop()
            stack.pop()
        else:
            # lesser priority can't be on top on higher or equal priority    
             # so pop and put in output   
            while(stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]):
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    return output

expr = input("Enter a boolean expression: ")
checkExpress(expr)
andSym(expr)
print('Infix expression: ',expr)
print('Postfix expression: ',infix_to_postfix(expr))

#arr = str.split(expr)
#infixToPostfix(len(expr), expr)
#print(expr)