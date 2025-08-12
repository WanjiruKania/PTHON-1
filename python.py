def simple_calculator(num1, num2, operation):
    """
    Performs a simple mathematical operation on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform.
                         Valid options are 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float: The result of the operation.
        str: An error message if the operation is invalid or a division by zero occurs.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        # Handle division by zero to prevent an error
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."

# --- Examples of how to use the function ---

# Addition
result_add = simple_calculator(10, 5, "add")
print(f"10 + 5 = {result_add}")

# Subtraction
result_subtract = simple_calculator(10, 5, "subtract")
print(f"10 - 5 = {result_subtract}")

# Multiplication
result_multiply = simple_calculator(10, 5, "multiply")
print(f"10 * 5 = {result_multiply}")

# Division
result_divide = simple_calculator(10, 5, "divide")
print(f"10 / 5 = {result_divide}")

# Division by zero
result_zero_division = simple_calculator(10, 0, "divide")
print(f"10 / 0 = {result_zero_division}")

# Invalid operation
result_invalid = simple_calculator(10, 5, "exponent")
print(f"Invalid operation example: {result_invalid}")