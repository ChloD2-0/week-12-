list1 = [1, 2, 3]
list2 = [4, 5, 6]
nested_list = [list1, list2] 
print(nested_list) # Output: [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2]) # Output: 6
print(nested_list[0][1]) # Output: 2

fruits = ["apple","orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats] 
groceries = [["apple","orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

# print(groceries[0])
# # fruits[0] = pineapple
# print(fruits)

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0 , "#"))
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
    
    

# for collection in groceries:
#     print(collection)

# print(groceries[1][2])
# print(groceries[0][2])
# print(groceries[2][2])





# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(matrix[0][2])    # 1
print(matrix[0][2])    # 3
print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]

example_list = [row[0] for row in matrix]
# for row in matrixL
#   print(row[0])
print(example_list)
    # [1, 4, 7]

# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
matrix2 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# Print the first list.
# first_list = [row[0] for row in matrix2]
# first_list2 = [row[1] for row in matrix2]
# first_list3 = [row[2] for row in matrix2]
# print(first_list)
print(matrix2[1])
# Print the second item from the third list.
print(matrix2[2][1])
# Use a list comprehension to extract the last item from each sub-list.
comprehension_list =[row[0] for row in matrix]
print(comprehension_list)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squared_numbers = [x**2 for x in range (1,11)]
# for x in range (1,11):
#   squared = x**2
#   print(squared)
print(squared_numbers)