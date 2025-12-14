users = []

def creat_user():
    print("\n --- Creat User ---")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    country = input("Enter country: ")
    hobby = input("Enter hobby: ")
    user = {
        "name": name,
        "age": age,
        "extra": {
            "country": country,
            "hobby": hobby,
        }
    }
    users.append(user)
    print("User created Successfully!")
    return user

def average_age():
    if not users:
        return 0
    return sum(u["age"] for u in users) / len(users)
def count_user():
    return len(users)
def filtered_by_min_age(min_age):
    return [u for u in users if u["age"] > min_age]
def show_user(user):
    print("\n --- User Infor ---")
    print(f"Name : {user['name']}")
    print(f"Age: {user['age']}")
    print("Extra:")
    for k, v in user['extra'].items():
        print(f" {k}: {v}")
def show_all_users():
    print("\n --- All User ---")
    if not users:
        print("No users available")
        return
    for u in users:
        show_user(u)

def main():
    while True:
        print("==== MENU ====")
        print("1. Create User")
        print("2 Show All users")
        print("3. show stats")
        print("4.filtered by minimum age")
        print(("5. Exit"))

        choice = input("Select an option: ")
        if choice == "1":
            creat_user()
        elif choice == "2":
            show_all_users()
        elif choice == "3":
            print("\n---Stats---")
            print(f"Total Users: {count_user()}")
            print(f"Average Age: {average_age()}")
        elif choice == "4":
            age = int(input("Minimum age: "))
            result = filtered_by_min_age(age)
            print("\n ---Result---")
            for u in result:
                show_user(u)
        elif choice == "5":
            print("Good bye.")
            break
        else:
            print("Invalid option")
if __name__ == "__main__":
    main()