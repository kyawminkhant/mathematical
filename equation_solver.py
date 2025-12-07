"""
Equation Solver
----------------
A custom expression interpreter that supports +, -, *, /, ^ and brackets,
with operator precedence and recursive evaluation.
"""

identifyAri=["+", "-", "*", "/", "^", "(", ")"] # Identifying Arithmetic sign
identifyNum=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # Identifying Numbers
targetReplace=-1 # For inserting the deleted part of the equation, case brackets

# Accept input and validate string
def equation():
    equate=str(input("Enter the equation: "))
    equateCheck=list(equate) # To validate the input easily
    
    for item in equateCheck: # Inspect each element of the list
        if (item not in identifyAri) and (item not in identifyNum) and item!=" " and item!=".": # Check if the element is not part of the list
            print("You have type unaccepted value. Please retype the equation.")
            return equation()
        
    if equateCheck.count("(")!=equateCheck.count(")"): # Complete the bracket
        print("Please complete the bracket.")
        return equation()
        
    if ")"==equateCheck[0]: # Case: )123-456
        print("You cannot put closing bracket at the beginning of the equation.")
        return equation()
            
    if any(op in equateCheck for op in identifyAri): # Checking if part of the identifyAri list is in equateCheck list
        if (equateCheck[len(equateCheck)-1] in identifyAri) and equateCheck[len(equateCheck)-1]!=")": # Re-request the input if there is arithmetic sign at the end of the input
            print("There cannot be arithmetic sign at the end of the equation.")
            return equation() # Recur the input request
        else:
            
            while " " in equateCheck: # Remove " " while are added by user based on their preferences
                equateCheck.remove(" ") # Reduce errors for next step
                
            return equateCheck
    else: # Re-request the input if there is not an arithmetic sign
        print("There is no arithmetic sign, therefore, this is just a number.")
        return equation() # Recur the input request
        
value=equation()



def numFix(equation):
    indexList=[]
    newEqn=[]
    tempNum=""
    
    for index in range(len(equation)): # Go through the list to find number and equation        
        if equation[index] in identifyNum or equation[index]==".":
            indexList.append(index) # Gather all index number if 
        else:
            if indexList!=[]:
                tempNum=""
                
                for i in indexList: # Fetch indexes where numeric string exit
                    tempNum+=equation[i] # Combine them into one string
                    
                newEqn.append(tempNum) # Add the fixed number into the newEqn list
                
                tempNum="" # Clear temporary storage
                indexList=[]
                
            newEqn.append(equation[index]) # Add the arithmetic sign into the newEqn list
            
    if indexList!=[]:
        tempNum=""
        for i in indexList: # Repeat one more time to allow last number to be added
            tempNum+=equation[i]
            
        newEqn.append(tempNum)
            
    return newEqn

       

def ariAssign(equation):
    
    if "(" in equation: # Bracket
        AllBracketLocate=[] # Store location data of every opening and closing bracket
        jump=0 # Count total opening bracket and find the innermost bracket
        InnerMostBracket=[] # Store innermost bracket location data
        InnerMostWork=[] # Store data within the innermost bracket
        
        for index in range(len(equation)):
            if equation[index]=="(":
                AllBracketLocate.append([index, "O"]) # Getting all indexes for Opening Bracket
                jump+=1 # Get to the innermost list
            elif equation[index]==")":
                AllBracketLocate.append([index, "C"])
                
        # Case 1: ((x+1)+y) (((x+1)+2)+y)
        for item in AllBracketLocate:
            if item[1]=="O": # Jump until the innermost bracket's opening
                jump-=1
                
            if jump==0:
                mark=item # Marked the item
                break
        
        InnerMostBracket.append(mark)
        InnerMostBracket.append(AllBracketLocate[AllBracketLocate.index(mark)+1])
        global targetReplace # Modify target to allow it to store outside of the subprogram
        targetReplace=InnerMostBracket[0][0]
        
        amountDel=InnerMostBracket[1][0]-InnerMostBracket[0][0]+1 # Size of the innermost bracket section
        
        for delete in range(amountDel): # Deleting the innermost bracket section fully
            InnerMostWork.append(equation.pop(InnerMostBracket[0][0]))
        
        InnerMostWork.remove("(") # Remove the Opening and the Closing Bracket included
        InnerMostWork.remove(")")
        
        result_inside=ariAssign(InnerMostWork) # Work on the innermost bracket section
        equation.insert(targetReplace, result_inside) # Replace the innermost bracket section with result
        return ariAssign(equation) # Repeat check

    elif "^" in equation:
        location=0
        num1=0
        num2=0
        
        for index in range(len(equation)):
            if "^"==equation[index]:
                location=index # Allow power from back to front
                
        num1=float(equation[location-1]) # Number before the sign
        num2=float(equation[location+1]) # Number after the sign
        result=num1**num2
        
        equation[location-1:location+2]=[str(result)] # Replace the section with the result
        return ariAssign(equation) # Repeat check
    
    elif "/" in equation:
        location=0
        num1=0
        num2=0
        
        for index in range(len(equation)):
            if "/"==equation[index]:
                location=index # Allow division from back to front
                
        num1=float(equation[location-1]) # Number before the sign
        num2=float(equation[location+1]) # Number after the sign
        try:
            result=round(num1/num2, 1)
        except ZeroDivisionError:
            print("Error! You can't divide by zero.")
            return ("Undefined") 
        
        equation[location-1:location+2]=[str(result)] # Replace the section with the result
        return ariAssign(equation) # Repeat check
    
    elif "*" in equation:
        location=0
        num1=0
        num2=0
        
        for index in range(len(equation)):
            if "*"==equation[index]:
                location=index # Allow multiplication from back to front
                
        num1=float(equation[location-1]) # Number before the sign
        num2=float(equation[location+1]) # Number after the sign
        result=num1*num2
        
        equation[location-1:location+2]=[str(result)] # Replace the section with the result
        return ariAssign(equation) # Repeat check
    
    elif "+" in equation:
        location=0
        num1=0
        num2=0
        
        for index in range(len(equation)):
            if "+"==equation[index]:
                location=index # Allow addition from back to front
                
        num1=float(equation[location-1]) # Number before the sign
        num2=float(equation[location+1]) # Number after the sign
        result=num1+num2
        
        equation[location-1:location+2]=[str(result)] # Replace the section with the result
        return ariAssign(equation) # Repeat check
    
    elif "-" in equation:
        location=0
        num1=0
        num2=0
        
        for index in range(len(equation)):
            if "-"==equation[index]:
                location=index # Allow subtraction from back to front
                
        num1=float(equation[location-1]) # Number before the sign
        num2=float(equation[location+1]) # Number after the sign
        result=num1-num2
        
        equation[location-1:location+2]=[str(result)] # Replace the section with the result
        return ariAssign(equation) # Repeat check
        
    if isinstance(equation, list) and len(equation)==1:
        return equation[0]
    return equation


        
        
print(f"The result of the equation is {ariAssign(numFix(value))}")


