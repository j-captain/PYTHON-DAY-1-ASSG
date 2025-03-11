def calculate(num1,num2,chosenOperation):
    if chosenOperation == '+':
        return(num1 + num2)
    elif chosenOperation == '-':
        return(num1 - num2)
    elif chosenOperation == '*':
        return(num1 * num2)
    elif chosenOperation == '/':
        if num2 == 0:
            return "Error!!!!Division by zero is not possible!!!"
        return(num1 / num2)
    else:
        return "Fatal Error!!!Re-enter operation!!!"
    
def main():
    num1 = float(input("Enter the first Number: "))
    num2 = float(input("Enter the second Number: "))

    chosenOperation = input("Enter Operation to Perform('+','-','*','/') : ")

    myResult = calculate(num1, num2, chosenOperation)

    print(f"{num1} {chosenOperation} {num2} = {myResult}")

if __name__ == "__main__":
    main()   
    