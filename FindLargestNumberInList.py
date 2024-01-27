numbers = [70 ,24, 37, 91 , 1002 ,43 ,101]
largest = numbers[0]
for i in numbers:
    if largest > i:
        continue
    else:
        largest = i

print(f"Largest Number : {largest}")