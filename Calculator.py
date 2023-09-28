#Allan Munjuri, SCT211-0624/2022

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Enter first number: ")
num1 = float(input())

print("Enter second number: ")
num2 = float(input())

print("Enter operation: ")
print("\n 1.Sum\n 2.Subtraction\n 3.Multiplication\n 4.Division\n")
operation = input()

if operation == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif operation == 2:
     print(num1, "-", num2, "=", subtract(num1, num2))

elif operation == 3:
     print(num1, "*", num2, "=", multiply(num1, num2))

elif operation == 4:
     print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input")
