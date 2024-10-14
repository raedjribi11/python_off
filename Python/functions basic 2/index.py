# Function 1: Countdown
def countdown(num):
    return list(range(num, -1, -1))

# Function 2: Print and Return
def print_and_return(my_list):
    print(my_list[0])
    return my_list[1]

# Function 3: First Plus Length
def first_plus_length(my_list):
    return my_list[0] + len(my_list)

# Function 4: Values Greater than Second
def values_greater_than_second(my_list):
    if len(my_list) < 2:
        return False
    
    second_value = my_list[1]
    new_list = [value for value in my_list if value > second_value]
    
    print(len(new_list))  # Print how many values are greater than the second
    return new_list

# Function 5: This Length, That Value
def length_and_value(size, value):
    return [value] * size

# Example usage:
# Countdown example
print("Countdown from 5:")
print(countdown(5))  # Output: [5, 4, 3, 2, 1, 0]

# Print and Return example
print("\nPrint and Return:")
result = print_and_return([1, 2])  # Output: 1
print(f"Returned value: {result}")  # Output: 2

# First Plus Length example
print("\nFirst Plus Length:")
print(first_plus_length([1, 2, 3, 4, 5]))  # Output: 6

# Values Greater than Second example
print("\nValues Greater than Second:")
print(length_and_value(6, 2))  # Output: [2, 2, 2, 2, 2, 2]