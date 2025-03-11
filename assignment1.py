def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."

# Main program
def main():
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Enter the operation (+, -, *, /): ")

    
    result = calculate(num1, num2, operation)

    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

# Run the program
if __name__ == "__main__":
    main()