 # @pro567722 Github
import sys
sys.set_int_max_str_digits(6000)

print("A simple calculator")
print("-------------------------")

while True:
    a = int(input("Enter your 1st number: "))
    b = int(input("Enter your 2nd number: "))

    print("Select an operator: 1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Raised to the power of\n")
    choice = int(input("Enter your choice: ").strip())
    if choice == 1:
        print(f"{a} + {b} = {a+b}")
    elif choice == 2:
        print(f"{a} - {b} = {a-b}")
    elif choice == 3:
        print(f"{a} / {b} = {a/b if not b == 0 else "Cannot Divide By Zero"}")
    elif choice == 4:
        print(f"{a} x {b} = {a*b}")
    elif choice == 5:
        try:
            print(f"{a} ^ {b} = {a**b}")
        except ValueError:
            print("Too large...try a smaller number (Upto 600 digits).")
    else:
        print("Invalid selection, choose from 1-5.")