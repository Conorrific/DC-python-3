#first_number = int(input("Enter first number "))
#second_number = int(input("Enter second number "))
#total = first_number + second_number
#print(f"The first number is {first_number}, the second number is {second_number}, bringing to total to {total}")


#make sure the indent is there, as anything outside of the indent is outside of the function.
#also make sure the function is doing only one thing.


first_number = int(input("Enter first number "))
second_number = int(input("Enter second number "))
#return bringsit outside the function. everything after the return wont run
def add(input_1,input_2):
    total = input_1 + input_2
    print("This needs to be before the return in order to work!")
    return total

some_variable = add(first_number,second_number)
print(some_variable)

#you can add a default value like "age = 22" otherwise need to specify
#you can call a function inside another function
def greet(first_name,last_name,age,address):
    print(f"first name is {first_name} and last name is {last_name}")
    #calling function inside another function example 'add(3,4)'
greet(last_name = 'John', first_name = 'Doe', age = 12, address = '1200 Richmond Ave')

