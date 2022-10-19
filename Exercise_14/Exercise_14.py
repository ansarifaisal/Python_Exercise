print("Please provide first number")
firstNumber = int(input())
print("Please provide second number")
secondNumber = int(input())
print("Please provide the operation you want to perform from the following: \n 1. + \n 2. - \n 3. * \n 4. /")
operation = input().lower()

if (firstNumber == 45) and (secondNumber == 3) and (operation.startswith("*")):
    print(555)
elif (firstNumber == 56) and (secondNumber == 9) and (operation.startswith("+")):
    print(77)
elif (firstNumber == 56) and (secondNumber == 4) and (operation.startswith("/")):
    print(4)
elif operation == "+":
    print(firstNumber + secondNumber)
elif operation == "-":
    print(firstNumber - secondNumber)
elif operation == "*":
    print(firstNumber * secondNumber)
elif operation == "/":
    print(firstNumber / secondNumber)
