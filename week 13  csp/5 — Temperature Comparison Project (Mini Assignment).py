# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:
# -10<x=<58 = cold
# 59=<x<84 = warm
# 84<x<110 = hot
x = int(input("What is the temperature today? "))

if x < -10:
    print(f"Extreme temperature warning!")
elif -10 <= x <= 58: 
    print("It is cold outside.")
elif 59 <= x <= 83:
    print("It is warm outside")
elif 84 <= x <= 110:
    print("It is hot outside")
else: 
    print("Extreme temperature warning!")