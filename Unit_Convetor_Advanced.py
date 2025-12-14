# Advanced Version of Unit Converter

CONVERSION = {
    "m": 1,
    "km": 1000,
    "cm": 0.01,
    "mm": 0.001,
    "dm": 0.1,
    "hm": 100,
    "dam": 10,
    "mile" : 1609.34,
    "yard" : 0.9144,
    "foot" : 0.3048,
    "feet" : 0.3048,
    "inch" : 0.0254,
    "inches" : 0.0254

}

print("Welcome to the Advanced Distance Unit Converter")

while True:
    c = input("Enter x to exit or press any key to continue: ").lower()
    if c == "x":
        print("Exiting the Unit Converter. Goodbye!")
        break

    a = input("Enter the unit you HAVE: ").lower()
    b = input("Enter the unit you WANT: ").lower()

    if a not in CONVERSION or b not in CONVERSION:
        print("Invalid unit selection. Try again.")
        print("\n-----------------------------\n")
        continue

    value = float(input("Enter the value you want to convert: "))

    # Step 1: Convert input to meters
    meters = value * CONVERSION[a]

    # Step 2: Convert meters to target unit
    result = meters / CONVERSION[b]

    print(f"{value} {a} is equal to {result} {b}")
    print("\n-----------------------------\n")
