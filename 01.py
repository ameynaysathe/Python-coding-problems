# 1. Write a program to find the largest of three numbers.

def largest_of_three(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3

# Example usage

print(largest_of_three(10, 20, 15))  # Output: 20
print(largest_of_three(-5, -10, -3))  # Output: -3
print(largest_of_three(0, 0, 0))      # Output: 0