counter = int(input())
list = []
filtered_list = []

for i in range(counter):
    num = int(input())

    list.append(num)

command = input()

for j in list:
    if command == 'even' and j % 2 == 0:
        filtered_list.append(j)

    elif command == 'odd' and j % 2 != 0:
        filtered_list.append(j)

    elif command == 'negative' and j < 0:
        filtered_list.append(j)

    elif command == 'positive' and j >= 0:
        filtered_list.append(j)

print(filtered_list)