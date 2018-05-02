num = int(input("Enter a number: "))
def game():
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print(f"Fizz")
    elif num % 5 == 0:
        print(f"Buzz")    
    else:
        print("Invalid number, sorry!")    
game()   