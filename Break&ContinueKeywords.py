#break
students = ["Usman", "Luqman", "Hamid", "Arslan", "Hussain", "Huzaifa"]

print("Break Example Below :")
for names in students:
    if names == "Hussain":
        break
    else:
        print(names)

print()
print("Continue Example Below :")
#continue
for names in students:
    if names == "Usman":
        continue
    else:
        print(names)