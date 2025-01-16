def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

#Example of the bug
my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}") #expect 0

my_list = [10,20,30]
result = calculate_average(my_list)
print(f"The average is: {result}") #expect 20

my_list = [10,20,30,40,50]
result = calculate_average(my_list)
print(f"The average is: {result}") #expect 30