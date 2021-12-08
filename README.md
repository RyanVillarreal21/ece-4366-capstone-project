# ece-4366-capstone-project

# This project is allows the user to input a boolean expression.
# Once the expression is entered, a function will check that the user
# entered a string that consisted of A-Z, +, ', and (). The program will
# terminate if the expression is invalid.
#
# Once a valid expression is entered, the program will add the symbol * to
# expression in between any variables that represent AND (ex. AB). The symbol
# is added to allow the function to parse the expression easier and convert it
# to postfix expression.
#
# Once the expression is in postfix, the program is meant to use the new expression
# to create a netlist that is used as a logic circuit. The program will then run the
# netlist into two functions that will generate the Combinational Controllability and
# the Combinational Observability. Once these functions have been evaluated, the netlist
# is used to detect all of the Stuck-At faults. The program will then go through the order
# of evaluating the netlist to find the Equivalent faults, Dominant faults, and the
# Collapse faults
#
# Currently only the user input to postfix conversion function properly