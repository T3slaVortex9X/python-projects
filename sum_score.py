

def total(numbers):
    t = 0
    for x in numbers:
        t += x
    return t
# Taking the numbers of subject
num_subject = int(input("How many subject do u have?"))
sum_score = []

for i in range(num_subject):
    print("Enter the score of subject:")
    grade = float(input(f"Subject {i+1}"))
    sum_score.append(grade)
    total_score = total(sum_score)
    average = total_score / num_subject

    print("\n Results")
    print(f"Your scores: {num_subject}")
    print(f"Your sum score is : {sum_score}")
    print(f"average: {average:.2f}")

    if average >= 17:
        print("status; Perfect")
    elif average >= 14:
        print("status: good")
    elif average >= 10:
        print("statu: passed")
    else:
        print("status:Failed")