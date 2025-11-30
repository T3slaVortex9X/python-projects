def total(numbers):
    t = 0
    for x in numbers:
        t += x
    return t
# Taking the numbers of subject
num_subject = int(input("How many subject do you have?: "))
# an empty list to get the scores in it
sum_score = []

for i in range(num_subject):
    print("Enter the score of subject: ")
    grades = float(input(f"Subject {i+1}"))
    sum_score.append(grades)
total_score = total(sum_score)

average = total_score / num_subject

print("Results")
print(f"Your scores: {num_subject}")
print(f"Your sum score: {sum_score}")
print(f"average: {average}")
