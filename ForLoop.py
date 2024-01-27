num = int(input("Enter The Number : \n"))
for i in range(num):
    print(i)


prices = [10 , 20, 30]
sumOfPrices = 0
for item in prices:
    sumOfPrices = sumOfPrices + item

print("Sum = ",sumOfPrices)


#Code for A Pattern. The Pattern Is :
#*****
#**
#*****
#**
#**
numbers = [5 , 2 , 5, 2, 2]

for i in numbers:
    print("*" * i )