#compile time
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for item in row:
        print(item)

#RunTime
rows = int(input("Enter Rows : "))
cols = int(input("Enter Columns : "))
myList = []
print("Enter Values : ")
for i in range(rows):
    list1 = []
    for j in range(cols):
        z = int(input())
        list1.append(z)

    myList.append(list1)

print(myList)