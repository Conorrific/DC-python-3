num1 = int(input("Enter a whole number: "))
opp = input("Enter the operation you would like to use: ")
num2 = int(input("Enter another whole number: "))
def add():
 if opp == "*":
     total = num1 * num2
     print(f"Your total is {total}")
 elif opp == "+":
     total = num1 + num2 
     print(f"Your total is {total}") 
 elif opp == "-":
     total = num1 - num2
     print(f"Your total is {total}")
 elif opp == "/":
     total = num1 / num2
     print(f"Your total is {total}")
 else:
     print("Invalid Entry, try again!")

add()