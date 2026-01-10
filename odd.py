


def get_numbers():

    while True:
        try:

            input_str = input("Enter the numbers with comma or space.")

            replaced = input_str.replace(',' ', ')
            splitted = replaced.split()
            numbers = [int(n) for n in splitted]
            return numbers if numbers else get_numbers()
        except ValueError:
            print("Enter number")
        except:
            print("Uounk error")
def process_data(data):
    unique_sorted = sorted(set(data))
    result = {}
    for i, num in enumerate(unique_sorted, 1):
        result[num] = {
            'type': 'even' if num % 2 == 0 else 'odd'
        }

    count = len(unique_sorted)
    if count <= 3:
        status = "low"
    elif count <= 6:
        status = "Medium"
    else:
        status = "high"

    return unique_sorted, result, status

def show_result(nums, result, status):
    print(f"unique numbers: {nums}")
    print(f"len: {len[nums]}")
    print(f"w: {status}")

def main():
    print("\n The Numbers analyser")
    data = get_numbers()
    unique_sorted, result, status = process_data(data)
    show_result(unique_sorted, result, status)
if __name__ == '__main__':
    main()