list = [8, 7, 2, 5, 3, 1]
target = 10

targetFoundNums = []
for i in list:
    for j in list:
        if i + j == 10:
            targetFoundNums.append([i, j])

for i in targetFoundNums:
    print(i)