#Created by Ryan Villarreal
 
OPERATORS = ['+', '*', "'", '(', ')']  # set of operators

#This function is used to evaluate the postfix expression to find faults
def findFaults(post):
    saFaults = 0
    eqFaults = 0
    colFaults = 0

    #Searches each index for an operator to assign SA faults and Equivalent faults
    for i in range(0, len(post), 1):
        if(post[i] not in OPERATORS):
            continue
        elif(post[i] == "*"):
            saFaults += 2  #Adds 2 SA faults for the gate
            eqFaults +=1   #Adds 1 SA0 fault for Equivalent fault
            print(str(i), "AND gate: ", "Found ", str(saFaults), "Stuck-At Faults and ", str(eqFaults), "Equivalent Faults")
            #The print line is used to show where the gate is found in the index of the expression
        elif(post[i] == "+"):
            saFaults += 2
            eqFaults += 1  #Adds 1 SA1 fault for Equivalent fault
            print(str(i), "OR gate: ", "Found ", str(saFaults), "Stuck-At Faults and ", str(eqFaults), "Equivalent Faults")
        elif(post[i] == "'"):
            saFaults += 2
            eqFaults += 2
            print(str(i), "NOT gate: ", "Found ", str(saFaults), "Stuck-At Faults and ", str(eqFaults), "Equivalent Faults")

    saFaults += 2   #SA0 and SA1 on output
    colFaults = saFaults - eqFaults  #SA faults left after removing Equivalent

    #Updates the generated report with fault calculations
    print("\n")
    f = open("report.txt", "a")
    f.write("Detected Stuck-At Faults: ")
    f.write(str(saFaults))
    f.write("\nDetected Equivalent Faults: ")
    f.write(str(eqFaults))
    f.write("\nDetected Collapsed Faults: ")
    f.write(str(colFaults))
    f.close()

    f = open("report.txt", "r")
    print(f.read())