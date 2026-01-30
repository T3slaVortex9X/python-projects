##-------------------------------
##--------------------------------

from random import choice
##0000-------------------00000

def is_weak_pw(password):
    score = 0
    if len(password) >= 8: score += 1
    elif any(c.isupper() for c in password): score += 1
    elif any(c.islower() for c in password): score += 1
    elif any(c.isdigit() for c in password): score += 1
    elif any(c in "!@#$%^&*?>" for c in password): score += 1
    return score
## This is the get strength function
def get_strength(score):
    if score <= 2: return "weak"
    elif score == 3: return "medium"
    elif score == 4: return "strong"
    else:
        return "very strong"
    ## Yeah the main function that control all function
def main():
    while True:
        print("\n" + "="*30)
        print("password strenght analyzer")
        print("1. Analyzer password")
        print("2. Exit")

        choice = input("select one of the above option")

        if choice == '1':
            analyze()
        elif choice == '2':
            break

while True:
    def analyze():
        print("---Password checker---")
    pw = input("Enter password: ")

    if is_weak_pw(pw):
        print("weak password")
        print("Your password is so weak plx enter a valid one")
    else:
        print("strong password")