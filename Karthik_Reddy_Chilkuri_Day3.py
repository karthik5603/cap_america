


#ADVANCED PROGRAMMING ASSIGNMENT - DAY 3
#KARTHIK REDDY CHILKURI
#MATRICULATION NUMBER: 100008159


# #1. Write a program to print multiplication table of a given number using FOR loop.
# number = int(input("Enter a number: "))
# print("Multiplication Table of", number)
# for i in range(1, 11):
#     print(number, "x", i, "=", number * i)




# #2. Write a program to greet all the person names stored in a list 'l' and which starts with S.
# l = ["Riya", "Shivam", "Sahil", "Rahul"]
# for name in l:
#     if name.startswith("S"):
#         print("Hello", name + "!")



# #3. Attempt problem 1 using WHILE loop.
# number = int(input("Enter a number: "))
# print("Multiplication Table of", number)
# i = 1
# while i <= 10:
#     print(number, "x", i, "=", number * i)
#     i += 1



# #4. Write a program to find whether a given number is prime or not.
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(num, "is not a prime number.")
#             break
#     else:
#         print(num, "is a prime number.")



# #5. Write a program to find the sum of first n natural numbers using WHILE loop.
# n = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("The sum of first", n, "natural numbers is:", sum)



# #6. Write a program to calculate the factorial of a given number using FOR loop.
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("The factorial of", num, "is:", factorial)



# #7. Write a program to print the following star pattern.

#                 #     *

#                 #    ***

#                 #   ***** for n = 3
# n = 3
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))




# #8. Write a program to print the following star pattern.
#                 #     *
#                 #     **
#                 #     *** for n = 3
# n = 3
# for i in range(1, n + 1):
#     print("*" * i)



# #9. Write a program to print the following star pattern.
# #     * * *
# #     *   * for n = 3
# #     * * *
# n = 3
# for i in range(n):
#     if i == 0 or i == n - 1:
#         print("* " * n)
#     else:
#         print("* " + "  " * (n - 2) + "*")



# # 10. Write a program to print multiplication table of n using for loops in reversed order.
# number = int(input("Enter a number: "))
# print("Multiplication Table of", number, "in reversed order:")
# for i in range(10, 0, -1):
#     print(number, "x", i, "=", number * i)





#FUNCTIONS



#1. Write a program using functions to find greatest of three numbers.
def greatest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(f"The greatest number is: {greatest_of_three(10, 25, 15)}")




#2. Write a python program using function to convert celsius to fahrenheit.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(f"30°C is {celsius_to_fahrenheit(30)}°F")




#3. How do you prevent a python print() function to print a new line at the end.
print("Hello, World!", end="")




#4. Write a recursive function to calculate the sum of first n natural numbers.
def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)
n = 5
print(f"The sum of first {n} natural numbers is: {sum_of_natural_numbers(n)}")





#5. Write a python function to priny the following pattern.
#        ***
#        **           for n = 3
#        * 
def print_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)
n = 3
print_pattern(n)




#6. Write a python function which converts inches to centimeters.
def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return centimeters
print(f"10 inches is {inches_to_centimeters(10)} centimeters")





#7. Write a python function to remove a given word at end("an" from "Rohan") from a list and strip it at the same time.
def remove_end_and_strip(word, suffix):
    clean_word = word.strip() 
    if clean_word.endswith(suffix):
        return clean_word[:-len(suffix)] 
    
    return clean_word
print(remove_end_and_strip("  Rohan  ", "an")) 




#8. Write a python function to print multiplication table of a given number.
def multiplication_table(number):
    print(f"Multiplication Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
multiplication_table(5)


