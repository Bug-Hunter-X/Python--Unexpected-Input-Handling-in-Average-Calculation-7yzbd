def calculate_average(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        return 0
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers")
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example demonstrating the robust solution
my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")  # Output: 0

my_list = [10, 20, 30]
result = calculate_average(my_list)
print(f"The average is: {result}")  # Output: 20

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}")  # Output: 30

try:
    result = calculate_average("not a list")
except TypeError as e:
    print(f"Caught TypeError: {e}") # Catches the error

try:
    result = calculate_average([10,20,'a'])
except ValueError as e:
    print(f"Caught ValueError: {e}") # Catches the error