


#ADVANCE PYTHON PROGRAMMING ASSIGNMENT - Day2
#KARTHIK REDDY CHILKURI
#MATRICULATION NUMBER: 100008159

##STRING

#1. Write a python program to display a user entered name followed byGood Morning using input() function.
name = input("Enter your name: ")
print(name + "!" + " Good Morning")


#2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

name_to_fill = "Karthik Reddy Chilkuri"
date_to_fill = "May 22, 2026"
letter = letter.replace("<|Name|>", name_to_fill)
letter = letter.replace("<|Date|>", date_to_fill)
print(letter)


#3. Write a program to detect double space in a string.
string = "ADVANCED  MATHEMATICS"
if "  " in string:
    print("Double space found!")
else:
    print("No double space found.")


#4. Replace the double space from problem 3 with single spaces.
string = string.replace("  ", " ")
print("String after replacing double spaces:", string)


#5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Class, lets learn python with me. Thanks!"
formatted_letter = letter.replace(" ", "\n")
print(formatted_letter)


##LIST AND TUPLE

#1. Write a program to store 5 colors in a list entered by the user.
colors = []
for i in range(5):
    color = input("Enter a color: ")
    colors.append(color)
print("The colors you entered are:", colors)


#2. Write a program to accept marks of 7 students and display them in a sorted manner.
marks = []
for i in range(7):
    mark = float(input("Enter marks for student {}: ".format(i + 1)))
    marks.append(mark)
marks.sort()
print("Marks in sorted order:", marks)


#3. Check that a tuple type cannot be changed in python.
my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)
try:
    my_tuple[0] = 99
except TypeError as e:
    print(f"Error caught successfully: {e}")
    print("Proof: Tuples cannot be changed after creation!")


#4. Write a program to sum a list with 5 numbers.
numbers = [10, 20, 30, 40, 50]
total_sum = sum(numbers)
print("The sum of the list is:", total_sum)


#5. Write a program to count the number of zeros in the following tuple:
    # a = (7, 0, 8, 0, 0, 9, 0, 4, 5, 0, 0, 0, 0)
a = (7, 0, 8, 0, 0, 9, 0, 4, 5, 0, 0, 0, 0)
zero_count = a.count(0)
print("The number of zeros in the tuple is:", zero_count)

