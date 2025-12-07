## This is a Mini Student Info Project
## This is like a Model
class Student:
    def __init__(self):
        print("---Wellcome to my Project---")

        self.name = input("Enter your name: ")

        while True:
            try:
                self.age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Invalid age - please Enter a valid integer.")

        while True:
            try:

                self.height = float(input("Enter your height: "))
                break
            except ValueError:
                    print("Please Enter a valid float or int")
      ## Display and output logic
    def show_info(self):
        print("\n --- Final Reasult ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")
## The Project Menue
def main():

        p = Student()  ## This is an object that contain the user info
        while True:
            print("-- Result --")
            print("1. Show info")
            print("2. Exit")
            choice = input("Slect an option")
            if choice not in ["1", "2"]:
                print("Invalid option")
                continue
            if choice == "2":
                print("Good bye")
                break
            if choice == "1":
                p.show_info()
if __name__ == "__main__":
    main()
