# invertrepeatednum (2).py

rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()
