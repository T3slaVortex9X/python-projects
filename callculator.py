## Simple Calculator



def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def power(a, b):
    return a ** b

def calculator():
    while True:

        print("---Simple Python Calculator---")
        print("Seclect Operation")
        print("1. Add")
        print("2. subtract")
        print("3. Multiply")
        print("4. divide")
        print("5. power")
        print("6. Exit")

        choice = input("Enter a number (1-5):")
        if choice == '6':
            print("Good bye")
            break

        if choice not in ['1', '2', '3', '4', '5']:

            print("Invalid Error!")
            return

        try:

           num1 = float(input("Enter your first number: "))
           num2 = float(input("Enter your second number: "))
        except ValueError:
          print("Invalid numbers Entered")
          return

        if choice == '1':

           print(f"Result: {add(num1, num2)}")
        elif choice == '2':
           print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {power(num1, num2)}")

if __name__ == "__main__":
    calculator()