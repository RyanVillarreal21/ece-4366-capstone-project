#Created by Ryan Villarreal

import math as mt
import string as st
import re
from collections import deque
from faults import findFaults

# Data structure to store a binary tree node
class node:
    def __init__(self, c):
        self.data = c
        self.left = None
        self.right = None

#The function ensures user only enters specific characters
def checkExpress(expr):
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
            print("Invalid boolean expression. Please restart program.")
            exit()
    return expr

OPERATORS = ['+', '*', "'", '(', ')']  # set of operators
PRIORITY = {'+':1, '*':1,"'":2} # dictionary having priorities 

def isOperators(c):
    return c == "+" or c == "*" or c == "'"

def andSym(expr):  #This function is used to add the symbol * for AND logic
    new_expr = []
    result = ''

    #The for loop is used to search the expression and insert * in between the needed variables
    for i in range(0, len(expr) - 1, 1):
        if(expr[i] not in OPERATORS and expr[i + 1] not in OPERATORS):
            new_expr += expr[i]
            new_expr.append("*")
            continue
        elif(expr[i] not in OPERATORS and expr[i + 1] == "("):
            new_expr += expr[i]
            new_expr.append("*")
            continue
        elif(expr[i] == ")" and expr[i + 1] not in OPERATORS):
            new_expr += expr[i]
            new_expr.append("*")
            continue
        elif(expr[i] not in OPERATORS and expr[i + 1] == "+"):
            new_expr += expr[i]
            new_expr.append("")
            continue
        elif(expr[i] not in OPERATORS and expr[i + 1] == "'"):
            new_expr += expr[i]
            new_expr.append("")
            continue
        elif(expr[i] == "'" and expr[i + 1] not in OPERATORS):
            new_expr += expr[i]
            new_expr.append("*")
            continue
        elif(expr[i] == "'" and expr[i + 1] == "("):
            new_expr += expr[i]
            new_expr.append("*")
            continue
        elif(expr[i] == ")" and expr[i + 1] == "+"):
            new_expr += expr[i]
            new_expr.append("")
            continue
        elif(expr[i] == ")" and expr[i + 1] == "'"):
            new_expr += expr[i]
            new_expr.append("")
            continue
        else:
            new_expr += expr[i]
            continue

    new_expr.insert(len(new_expr), expr[-1])  #Adds the last string index to stack
    temp = []

    while new_expr:  #if stack is not empty, reverse the order of stack
        temp.append(new_expr.pop())
    for item in temp:
        new_expr.append(item) #append item to stack
    while new_expr:
        result += new_expr.pop()

    return result

def infix_to_postfix(expr): #input expression converted to postfix
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

# def add(post):
#     # If its the end of the expression
#     if(post == ''):
#         return ''
 
#     # If the character is an operand
#     if(post[0] >= 'A' and post[0] <= 'Z'):
#         return node(post[0]), post[1:]
#     else:
#         # Create a node with a[0] as the data and
#         # both the children set to null
#         p = node(post[0])
#         # Build the left sub-tree
#         p.left,q = add(post[1:])
#         # Build the right sub-tree
#         p.right,q = add(q)
#         return p,q

# # Function to construct an expression tree from the given postfix expression
# def construct(post):
#     root = None
#     stack = []
#     while(post):
#         curr = post.pop()
#         curr_node = Node(curr)
#         if(not root):
#              root = curr_node
#         if(stack):
#             parent, side = stack.pop()
#         if(side == 0):
#             parent.left = curr_node
#         else:
#             parent.right = curr_node
#         if(not curr.isletter()):
#             stack.append((curr_node, 0))
#             stack.append((curr_node, 1))
#     return root

# def height(root):
#     if root is None:
#         return 0
#     else:
#         # Compute the height of each subtree
#         lheight = height(root.left)
#         rheight = height(root.right)
 
#         # Use the larger one
#         if lheight > rheight:
#             return lheight + 1
#         else:
#             return rheight + 1

# # Function to  print level order traversal of tree
# def printLevelOrder(root):
#     h = height(root)
#     for i in range(1, h + 1):
#         printCurrentLevel(root, i)
#         print("\n\n")
 
 
# # Print nodes at a current level
# def printCurrentLevel(root, level):
#     if root is None:
#         return
#     if level == 1:
#         print(root.data, end = " ")
#     elif level > 1:
#         printCurrentLevel(root.left, level - 1)
#         printCurrentLevel(root.right, level - 1)

if __name__ == '__main__':
    expr = input("Enter a boolean expression [please include () wherever possible]: ")
    checkExpress(expr)

    #Sends boolean expression to be adjusted before being converted to postfix
    infix = andSym(expr)
    print("Infix expression: ", infix)
    post = infix_to_postfix(infix)
    print("Postfix expression: ", post)
    print("\n")

    #Begins generating the report of the program
    f = open("report.txt", "w")
    f.write("Report for Detected Faults and SCOAP\n")
    f.write("\nOriginal Boolean Expression: ")
    f.write(expr)
    f.write("\nInfix Expression: ")
    f.write(infix)
    f.write("\nPostfix Expression: ")
    f.write(post)
    f.write("\n\n")
    f.close()
    findFaults(post) #Calls the findFaults function in faults.py
