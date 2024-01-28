numbers = [97 , 92 , 91 , 97 , 92 ,65 ,47 ,83]

for item in numbers:
    if numbers.count(item) > 1:
        numbers.remove(item)

print(numbers)