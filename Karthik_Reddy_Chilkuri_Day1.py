

# ADVANCED PROGRAMMING ASSIGNMENT - DAY 1
# KARTHIK REDDY CHILKURI
# MATRICULATION NUMBER: 100008159


# 1. Write a python program to add two numbers.
num1 = 5
num2 = 10
result = num1 + num2
print("The sum of the two numbers is:", result)


# 2. Write a python program to find remainder when a number is divided by z.
number = 17
z = 5
remainder = number % z
print("The remainder is:", remainder)


# 3. Check the type of variable assigned using input () function.
data = input("Enter something:  ")
print("The type of the variable is:", type(data))


#4. Use comparison operator to find out whether 'a' given variable is greater than'b' or not. Take a = 34 and b= 80
a = 34
b = 80
if a > b:
    print("Yes, 'a' is greater than 'b'.")
else:
    print("No, 'a' is not greater than 'b'.")

#5. Write a python Program to find an average of two numbers entered by the user.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
average = (num1 + num2) / 2
print("The average of the two numbers is:", average)


#6. Write a pythonProgram to calculate the square of a number entered by the user.
number = float(input("Enter a number to find its square: "))
square = number ** 2
print("The square of the number is:", square)