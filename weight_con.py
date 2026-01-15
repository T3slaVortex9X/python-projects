##This is a mini project that cover  calculating the weight and change it
weight = float(input("Enter your weight: "))
unit = input("Pound or Kilograms? (K or L")

if unit == "K" or "k":
    weight = weight * 2.205
    unit = "LBS"
elif unit == "L" or "l":
    weight = weight / 2.205
    unit = "KGS"
else:
    print("Invalid option")
print(f"Your weight is: {round(weight, 1)} {unit}")