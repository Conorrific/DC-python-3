outside = float(input("Enter a temperature, and I'll convert it: "))
temptype = input("is this celcius or fahrenheit? answer with c or f ")
if temptype == "c":
    newtemp = str(round((outside * 1.8) + 32, 2))
    print("Your temperature in Fahrenheit is " + newtemp + " degrees!", 2)
elif temptype == "f":
    newtemp = str(round((outside - 32 ) / 1.8, 2))
    print("Your temperature in Celcius is " + newtemp + " degrees!", 2)
else:
    print("Invalid answer, sorry!")
