## Simple python
##----------------------------------------------
##--------------------------------------------

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == "0":  ## Error of division by zero
        return "Error, Division by zero"
    return a / b
def power(a, b):
    return a ** b
def calculator():
    history = []


    while True:
        print("\n---Simple CL Calculato---")
        print("Select operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. History")
        print("7. Exit")

        choice = input("Enter a Number (1-6)")
        if choice == "7":
            print("Exiting...")
            break
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid Error")
            return
        if choice == "6":
            if not history:
                print("\nNo calculation history yet!")
            else:
                print("\n----Calculatio History----")
                i = 0
                while i < len(history):
                    print(f"{i+1}. {history[i]}")
                    i += 1
                    print("-" * 25)
                    return


        try:
            num1 = float(input("Enter your First Number: "))
            num2 = float(input("Enter your Second Number: "))
        except ValueError:
            print("Enter a Valid number")
            continue
        result = None
        operation = ""

        if choice == "1":
            result = add(num1, num2)
            operation = f"{num1} + {num2} = {result}" ##Saving the operation on history list

        elif choice == "2":
            result = subtract(num1, num2)
            operation = f"{num1} - {num2} = {result}"
        elif choice == "3":
            result = multiply(num1, num2)
            operation = f"{num1} * {num2} = {result}"
        elif choice == "4":
            result = divide(num1, num2)
            operation = f"{num1} / {num2} = {result}"
        elif choice == "5":
            result = power(num1, num2)
            operation = f"{num1} ** {num2} = {result}"
        print(f"Result: {result}")
        history.append(operation)

        continue_cal = input("\nDo you want to perform another calculation? (yes/No")
        if continue_cal.lower() != "yes":
            print("Good bye")
            break


if __name__ == "__main__":
    calculator()
