try:
    first_number = int(input("Enter First Number : "))
    second_number = int(input("Enter Second Number : "))
    result = first_number / second_number
    print(f"Result : {result}")
except ZeroDivisionError:
    print("Number Cannot Be Divided By Zero.")
except ValueError:
    print("Please Enter Values In Number..")