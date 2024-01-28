#Dictionary

studentInfo = {130: "Muhammad Usman", 101: "Luqman"}
print(studentInfo)

studentInfo[130] = "Usman"
print(studentInfo)

# studentInfo.popitem()
# print(studentInfo)

phone = input("Phone : ")
output = ""
digitsMapping = {
    "1":"One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

for ch in phone:
    if ch in digitsMapping:
        print(digitsMapping.get(ch))
    # output += digitsMapping.get(ch, "!")

# print(output+"")