

Converter = {
    'c_to_f': lambda c: (c * 9/5) + 32,
    'f_to_c': lambda f: (f - 32) * 5/9
}
print("\n---Wellcome to Temperature Converter---")
print("You can enter 'q' at anytime to quite")

while True:
    print("Lets goo")
    print("1. Celsius to Farenheit")
    print("2. Farenheit to Celsius")

    choice = input("\n choose one of them (1, 2) or 'q' for quite: ")
    if choice.lower() == "q":
        print("good bye")
        break
    if choice not in ['1', '2']:
        print("Invalid option")
        continue
    while True:
        temp_input = input(f"\n Enter temperature (or 'b' for back): ")
        if temp_input.lower() == 'b':
            break
        elif temp_input.lower() == 'q':
            print("Good bye")
            exit()

        try:
            temp = float(temp_input)
            if choice == 1:
                result = Converter['c_to_f'](temp)
                print(f"{temp} = {result:.1f}")
            else:
                result = Converter['f_to_c'](temp)
                print(f"{temp} = {result:.1f}")
        except ValueError:
                print("Plx Enter a Valid number")