

Converter = {
    'c_to_f': lambda c: (c * 9/5) + 32,
    'f_to_c': lambda f: (f - 32) * 5/9
}
#print(f" {Converter['c_to_f'](25):.1f}f")
print("\n---Wellcome to my project---")
print("1.Change c to f")
print("2.Change f to c")
choice = int(input("select an option: "))
if choice not in [1, 2]:
    print("Invalid choice")
elif choice == 1:
    print(f" {Converter['c_to_f'](25):.1f}f")
elif choice == 2:
    print(f" {Converter['f_to_c'](77):.1f}f")