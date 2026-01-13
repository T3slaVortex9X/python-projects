import time

users = []

def creat_user():
    print("\n---Wellcome---")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    country = input("Enter your country: ")
    hobby = input("Enter your hobby: ")
    user = {
        "name": name,
        "age": age,
        "extra": {
            "hobby": hobby,
            "country": country
        }
    }
    users.append(user)
    print("Users Created successfully!")
    return user
def average_age():
    if not users:
        return 0
    return sum(u["age"] for u in users) / len(users)
def count_user():
    return len(users)
def filtered_by_min_age(min_age):
    return (u for u in users if u["age"] > min_age)
def show_user(user):
    print("\n---Users---")
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print("Extra:")
    for k, v in user['extra'].items():
        print(f" {k}: {v}")
def show_all_user():
    if not users:
        print("No users")
        return
    for u in users:
        show_user(u)
def main():
    while True:
        print("\n--Wellcome to Projects--")
        print("1.Creating user")
        print("2.Show all users")
        print("3.Show stats")
        print("4.filtered by min age")
        print("5.Exit")

        choice = int(input("select an option: "))
        if choice not in [1, 2, 3, 4, 5]:
            print("Select existing option")
        elif choice == 1:
            creat_user()
        elif choice == 2:
            show_all_user()
        elif choice == 3:
            print("--STATS")
            print(f"Total user: {count_user()}")
            print(f"Average age: {average_age()}")
        elif choice == 4:
            age = int(input("enter the minimum age"))
            result = filtered_by_min_age(age)
            print("--Result--")
            for u in result:
                show_user(u)
        elif choice == 5:
            print("Good bye!")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("...........")
            time.sleep(1)
            print(".......................")
            time.sleep(1)
            print("..................................")
        else:
            print("Invalid option")
if __name__ == "__main__":
    main()