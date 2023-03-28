# Data Types

# String

print("Hello"[4])

# Integer

print(123 + 345)

print(123_456_789)

# Float

print(3.14159)

# Boolean

print(True)
print(False)


# Practices Data Types

num_char = len(input("What is your name\n"))
new_num_char = str(num_char)
print("Your name has "+ str(num_char)+ " characters.")

print("Your name has "+ new_num_char + " characters.")

print(type(num_char))

# Practice Challenge of

two_digit_number = input("Type a two digit number\n")

first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])
two_digit_number_sum = first_number + second_number
print(two_digit_number_sum)


# BMI Calculator:



height = input("enter your height in m: \n")
weight = input("Enter your weight in kg: \n")

height_float = float(height)
weight_float = float(weight)

BMI = (weight_float / (height_float**2))
BMI_as_int = int(BMI)

print(BMI)
print(BMI_as_int)
