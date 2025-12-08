print("Welcome To Square & Cube Calculator")

operation = input("""
Enter 2 for Square"  
Enter 3 for Cube
                  """)

a = int(input("Enter The Number :"))

if operation == '2':
    print(f"THe Square Of Given Number is {a*a}")

elif operation == '3':
    print(f"The Cube of Given Number is {a*a*a}")

else:
    print("Invalid Input, Please Enter Valid Input ")

print("Thanks For Using Whatever This Is")
    