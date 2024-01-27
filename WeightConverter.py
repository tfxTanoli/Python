weight = int(input("Enter Your Weight : "))
selectTypeOfWeight = input('Press L or l for lbs or k or K for Kg : ')

if selectTypeOfWeight.lower() == 'k':
    weight = weight * 0.45
    print(f"Your Weight is {weight} kilos")
elif selectTypeOfWeight.lower() == 'l':
    weight = weight / 0.45
    print(f"Your Weight is {weight} pounds")
else:
    print("Invalid Unit")
