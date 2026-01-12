"""Hello this is a mini student info project"""
import time
class Student():
    def __init__(self):
        print("---Wellcome to Student Info Projects---")

        self.name = input("Enter your name: ")

        while True:
            try:
                self.age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Please, Enter a Valid Number.")
        while True:
            try:
                self.high = float(input("Enter your high: "))
                break
            except ValueError:
                print("Please, Enter a Valid number")
    def show_info(self):
        print("\n---Final Result---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"High: {self.high}")
def main():
    p = Student()
    while True:
        print("\n---Result---")
        print("1.Show Info")
        print("2.Exit")

        choice = int(input("Select an option: "))
        if choice not in [1, 2]:
            print("Invalid choice")
            continue
        elif choice == 2:
            print("Good bye")
            print("...")
            time.sleep(2)
            print(".....")
            time.sleep(2)
            print(".........")
            time.sleep(3)
            print(".............")
            time.sleep(4)
            print("....................")
            break
        elif choice == 1:
            p.show_info()
if __name__ == "__main__":
    main()
