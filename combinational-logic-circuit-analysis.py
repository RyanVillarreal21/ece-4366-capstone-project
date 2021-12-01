import math as mt
import string as st
import re

def checkExpress(expr):   #The function ensures user only enters specific characters
    n = len(expr)
    #print(n)
    for i in range(n):
        if(expr[i] == 'A'):
            continue
        elif(expr[i] == 'B'):
            continue
        elif(expr[i] == 'C'):
            continue
        elif(expr[i] == 'D'):
            continue
        elif(expr[i] == 'E'):
            continue
        elif(expr[i] == 'F'):
            continue
        elif(expr[i] == 'G'):
            continue
        elif(expr[i] == 'H'):
            continue
        elif(expr[i] == 'I'):
            continue
        elif(expr[i] == 'J'):
            continue
        elif(expr[i] == 'K'):
            continue
        elif(expr[i] == 'L'):
            continue
        elif(expr[i] == 'M'):
            continue
        elif(expr[i] == 'N'):
            continue
        elif(expr[i] == 'O'):
            continue
        elif(expr[i] == 'P'):
            continue
        elif(expr[i] == 'Q'):
            continue
        elif(expr[i] == 'R'):
            continue
        elif(expr[i] == 'S'):
            continue
        elif(expr[i] == 'T'):
            continue
        elif(expr[i] == 'U'):
            continue
        elif(expr[i] == 'V'):
            continue
        elif(expr[i] == 'W'):
            continue
        elif(expr[i] == 'X'):
            continue
        elif(expr[i] == 'Y'):
            continue
        elif(expr[i] == 'Z'):
            continue
        elif(expr[i] == '+'):
            continue
        elif(expr[i] == "'"):
            continue
        elif(expr[i] == "("):
            continue
        elif(expr[i] == ")"):
            continue
        else:
            # if(expr[i] != ''):
            expr = input("Invalid boolean expression. Please enter another: ")
            checkExpress(expr)
            # else:
            #     print("Evaluation success")
            #     break
    return expr

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

OPERATORS = ['+', '*', "'", '(', ')']  # set of operators
PRIORITY = {'+':1, '*':1,"'":2} # dictionary having priorities 

def andSym(expr):  #This action is used to add the symbol * for AND logic
    new_expr = []
    result = ''

    for i in range(0, len(expr) - 1, 1):
        if(expr[i] not in OPERATORS and expr[i + 1] not in OPERATORS):
            new_expr += expr[i]
            new_expr.append("*")
            # i += 1
            continue
        elif(expr[i] not in OPERATORS and expr[i + 1] == "("):
            #new_expr = new_expr[:i + 1] + '*' + new_expr[i + 1:]
            new_expr += expr[i]
            new_expr.append("*")
            # i += 1
            continue
        elif(expr[i] == ")" and expr[i + 1] not in OPERATORS):
            #new_expr = new_expr[:i + 1] + '*' + new_expr[i + 1:]
            new_expr += expr[i]
            new_expr.append("*")
            # i += 1
            continue
        elif(expr[i] not in OPERATORS and expr[i + 1] == "+"):
            new_expr += expr[i]
            new_expr.append("")
            # i += 1
            continue
        elif(expr[i] not in OPERATORS and expr[i + 1] == "'"):
            new_expr += expr[i]
            new_expr.append("")
            # i += 1
            continue
        elif(expr[i] == "'" and expr[i + 1] not in OPERATORS):
            new_expr += expr[i]
            new_expr.append("*")
            # i += 1
            continue
        elif(expr[i] == "'" and expr[i + 1] == "("):
            new_expr += expr[i]
            new_expr.append("*")
            # i += 1
            continue
        elif(expr[i] == ")" and expr[i + 1] == "+"):
            #new_expr = new_expr[:i + 1] + '*' + new_expr[i + 1:]
            new_expr += expr[i]
            new_expr.append("")
            # i += 1
            continue
        elif(expr[i] == ")" and expr[i + 1] == "'"):
            #new_expr = new_expr[:i + 1] + '*' + new_expr[i + 1:]
            new_expr += expr[i]
            new_expr.append("")
            # i += 1
            continue
        else:
            new_expr += expr[i]
            # i += 1
            continue
    new_expr.insert(len(new_expr), expr[-1])  #Adds the last string index to stack
    temp = []
    while new_expr:  #if stack is not empty, reverse the order of stack
        temp.append(new_expr.pop())
    for item in temp:
        new_expr.append(item) #append item to stack
    while new_expr:
        result += new_expr.pop()

    # for i in range(0, n, 2):
    #     if(expr[i + 1] == "+"):
    #         i += 1
    #         continue
    #     elif(expr[i + 1] == "'"):
    #         i += 1
    #         continue
    #     elif(expr[i + 1] == "("):
    #         i += 1
    #         continue
    #     elif(expr[i + 1] == ")"):
    #         i += 1
    #         continue
    #     else:
    #         expr = expr[:i] + '*' + expr[i:]
    #         #res = "".join((expr[:i], '*', expr[i:]))
    #         i += 1
    #         continue
    return result

def infix_to_postfix(expr): #input expression
    stack = [] # initially stack empty
    postfix = '' # initially output empty

    for ch in expr:
        if(ch not in OPERATORS):  # if an operand then put it directly in postfix expression
            postfix += ch
        elif(ch == '('):  # else operators should be put in stack
            stack.append('(')
        elif(ch == ')'):
            while(stack and stack[-1] != '('):
                postfix += stack.pop()
            stack.pop()
        else:
            # lesser priority can't be on top on higher or equal priority    
             # so pop and put in output   
            while(stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]):
                postfix += stack.pop()
            stack.append(ch)
    while stack:
        postfix += stack.pop()
    return postfix

expr = input("Enter a boolean expression: ")
checkExpress(expr)
infix = andSym(expr)
print("Infix expression: ", infix)
print("Postfix expression: ",infix_to_postfix(infix))