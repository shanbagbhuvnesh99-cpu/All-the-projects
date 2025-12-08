print("Welcome To Unit Converter")

print("""
Press 1 for GB to MB
Press 2 for MB to KB
""")

choice = input("Enter your choice of unit: ")

if choice == "1":
    gb = float(input("Please enter file size in GB: "))
    print(f"The size of file in MB is {gb * 1024} MB")

elif choice == "2":
    mb = float(input("Please enter file size in MB: "))
    print(f"The size of file in KB is {mb * 1024} KB")

else:
    print("Invalid choice. Please enter 1 or 2.")
