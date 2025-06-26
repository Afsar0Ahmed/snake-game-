def sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] < list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                temp = list[j + 1]


list = (3, 5, 6, 7, 2, 4)
sort(list)
print(list)
