#Calculator
firstNumber = input("Enter 1st Number : ")
secondNumber = input("Enter 2nd Number : ")

choice = input(
    'Enter The Operation.\nFor 1.Addition\t2.Subtraction\t3.Multiplication\t4.Division\t5.Finding Remainder\t6.Power\n')
choice = int(choice)
if choice == 1:
    result = int(firstNumber) + int(secondNumber)
    print(result)
elif choice == 2:
    result = int(firstNumber) - int(secondNumber)
    print(result)
elif choice == 3:
    result = int(firstNumber) * int(secondNumber)
    print(result)
elif choice == 4:
    if int(secondNumber)>0:
        result = float(firstNumber) / float(secondNumber)
        print(result)
    else:
        print("Number Cannot Be Divided By Zero.")
elif choice == 5:
    result = float(firstNumber) % float(secondNumber)
    print(result)
elif choice == 6:
    result = int(firstNumber) ** int(secondNumber)
    print(result)
else:
    print("Invalid Operation")