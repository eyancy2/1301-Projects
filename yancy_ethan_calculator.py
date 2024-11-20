"""
Author: Ethan Yancy
Description: This is a simple terminal calculator. It takes an expression in the format
'left operator right' and calculates the result. It supports +, -, *, /, %, **, and //.
The program shows errors for invalid operators or formats. The user can enter multiple 
expressions until they type 'quit' or 'q' to exit.
"""

def add(left, right):
    return left + right

def subtract(left, right):
    return left - right

def multiply(left, right):
    return left * right

def divide(left, right):
    if right == 0:
        return "Error: Division by zero"
    return left / right

def modulus(left, right):
    return left % right

def power(left, right):
    return left ** right

def floor_divide(left, right):
    if right == 0:
        return "Error: Division by zero"
    return left // right

def parse_expression(expression):
    parts = expression.split()  # Split the input into parts
    if len(parts) != 3:  # Check if there are exactly three parts
        return None, None, None

    # Try to convert the left and right parts to numbers
    try:
        left = float(parts[0]) if '.' in parts[0] or 'e' in parts[0] else int(parts[0])
        operator = parts[1]
        right = float(parts[2]) if '.' in parts[2] or 'e' in parts[2] else int(parts[2])
    except ValueError:
        return None, None, None  # If conversion fails, return None

    return left, operator, right

def calculate(left, operator, right):
    # Check which operator is used and call the appropriate function
    if operator == '+':
        return add(left, right)
    elif operator == '-':
        return subtract(left, right)
    elif operator == '*':
        return multiply(left, right)
    elif operator == '/':
        return divide(left, right)
    elif operator == '%':
        return modulus(left, right)
    elif operator == '**':
        return power(left, right)
    elif operator == '//':
        return floor_divide(left, right)
    else:
        return "Error: Invalid operator. Use +, -, *, /, %, **, or //."

def main():
    print("Welcome to the terminal calculator!")
    print("Enter expressions like '5 + 3'.")  # Example format
    print("Type 'quit' or 'q' to exit.")  # Exit instructions
    
    while True:
        expression = input("Enter expression: ").strip()  # Get input from the user
        
        if expression.lower() in {'quit', 'q'}:  # Check for quit commands
            print("Exiting the calculator. Goodbye!")
            break
        
        left, operator, right = parse_expression(expression)  # Parse the expression
        
        # Check if parsing was successful
        if left is None or operator is None or right is None:
            print("Error: Invalid expression format. Use 'left operator right'.")
            continue  # Skip to the next iteration
        
        result = calculate(left, operator, right)  # Calculate the result
        print(f"Result: {result}")  # Print the result

if __name__ == "__main__":
    main()
