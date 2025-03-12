import time
import os

firstVal = 0
secVal = 0
op = ''
opList = ['+', '-', '*', '/']
errControl = False

#flush operator
def flushOpAndCalculate(firstVal, secVal, op):
    if op == opList[0]:
        return "Result is: " + str(firstVal + secVal)
    elif op == opList[1]:
        return "Result is: " + str(firstVal - secVal)
    elif op == opList[2]:
        return "Result is: " + str(firstVal * secVal)
    elif op == opList[3]:
        return "Result is: " + str(firstVal / secVal)
    else:
        return "No Operator Available " + op

def interact():
    interact = input("Do you want to restart the program (Y/N)? ")
    if interact == "Y" or interact == "y":
        os.system('cls')
        time.sleep(1)
        program()
    elif interact == "N" or interact == "n":
        print("Quitting.")
        time.sleep(1)
        os.system('cls')
    else:
        interact()

def program():
    os.system('cls')
    try:
        firstVal = int(input("Give the first number: "))
        secVal = int(input("Give the second number: "))
        op =  input(
        "+ | Adding" +"\n"+
        "- | Subtracting" +"\n"+
        "* | Multipling" + "\n"+
        "/ | Dividing" +"\n" +
        "Select Operation: ")

        print("Processing.")    
        time.sleep(1)
        os.system('cls')

        result = flushOpAndCalculate(firstVal, secVal, op)
        print(result)

        interact()

    except:
        print("Please enter a number.")
        
        time.sleep(1)
        os.system('cls')
        program()

program()

