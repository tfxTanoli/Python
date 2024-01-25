# list1 = [97,95,98]
# list2 = [100,99,91]
# list1 = list1.__add__(list2)
# print(list1)

marks = [91, 92, 93]
# for finalMarks in marks:
#     print(finalMarks)
marks.append(99)
print(marks)

marks.insert(2, 87)
print(marks)

marks.sort()
print(marks)

marks.reverse()
print(marks)

print(marks.__contains__(101))

#while loop
i = 0
while i <= len(marks):
    print(marks[i])
    i += 1
