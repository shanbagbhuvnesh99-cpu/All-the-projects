print("Welcome To Distance Unit Calculator")

while True:
    print("""
1. Kilometers to Miles
2. Miles to Kilometers
3. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == '1':
        km = float(input("Enter distance in Kilometers: "))
        print(f"{km} km = {km * 0.621371:.3f} miles")

    elif choice == '2':
        miles = float(input("Enter distance in Miles: "))
        print(f"{miles} miles = {miles / 0.621371:.3f} km")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Enter 1, 2, or 3.")
