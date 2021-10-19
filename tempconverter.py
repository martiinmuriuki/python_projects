import math
import time

# Function
def again():
    try_again = print()
    User_Temp = input("your temperature,'C' for celsius, 'F' for fahrenheit 'K' for kelvin:  ").upper()
    convert_Temp = input("The temperature you want to convert to, 'C' for celsius, 'F' for fahrenheit 'K' for kelvin: ").upper()
  
    # conversion  equations
    if User_Temp == "C":
        if convert_Temp == "F":
            degree = float(input("enter the degree: "))
            result = (degree * 9/5) + 32
            print(f"{result}°F")
        elif convert_Temp == "K":
            degree = float(input("enter the degree: "))
            result = degree + 273.15
            print(f"{result}°K")
        elif convert_Temp == "C":
            print("This is the same type of temperature")
            time.sleep(1)
            again()
        else:
            print("Type a temperature")
            time.sleep(10)
            again()

    elif User_Temp == "F":
        if convert_Temp == "C":
            degree = float(input("enter the degree: "))
            result = (degree - 32) * 5/9
            print(f"{result}°C")
        elif convert_Temp == "K":
            degree = float(input("enter the degree: "))
            result = (degree - 32) * 5/9 + 273.15
            print(f"{result}°K")
        elif convert_Temp == "F":
            print("This is the same type of temperature")
            time.sleep(10)
            again()
        else:
            print("Type a unit")
            time.sleep(10)
            again()

    elif User_Temp == "K":
        if convert_Temp == "C":
            degree = float(input("enter the degree: "))
            result = degree - 273.15
            print(f"{result}°F")
        elif convert_Temp == "F":
            degree = float(input("enter the degree: "))
            result = (degree - 273.15) * 9/5 + 32
            print(f"{result}°K")
        elif convert_Temp == "K":
            print("This is the same type of temperature")
            time.sleep(10)
            again()
        else:
            print("Type a unit")
            time.sleep(10)
            again()

    else:
        print("Type a temperature")
        time.sleep(10)
        again()

# try again
    while try_again != "Yes" and try_again != "No":
        print("Do you want to try again?")
        try_again = input("Yes | No | ").lower().capitalize()
        if try_again == "Yes":
            again()
            break
        elif try_again == "No":
            print("Goodbye")
            break

again()