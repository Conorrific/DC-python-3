import calc2
#make dis shit repeatpeatpeatpeatpeat and ask the user if they would like to continue.
#  If they would like to make it loop. Otherwise give them the option to quit
def math():
    input1 = float(input("Enter a whole number: "))
    opp = input("Enter the operation you would like to use: ")
    input2 = float(input("Enter another whole number: "))
    if opp == "*":
         calc2.multiply(input1,input2)
    elif opp == "+":
        calc2.add(input1,input2)
    elif opp == "-":
        calc2.sub(input1,input2)   
    elif opp == "/":   
        calc2.divide(input1,input2)
    else:
        print("Invalid entry")
math()        

redo = input("Would you like to do another calculation? Answer 'yes' or 'no " )
redo.lower()
if redo == "yes":
    math()
else:
    print("have a good day!")

