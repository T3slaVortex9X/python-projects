data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

uniq_sorted = sorted(set(data))
result = {}

for num in uniq_sorted:
    if num % 2 == 0:
        result[num] = "even"
    else:
        result[num] = "odd"

match len(result):
    case 1:
        status = "low"
    case 2:
        status = 'medium'
    case 3:
        status = 'high'
print(result)
print(status)