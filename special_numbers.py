number = int(input())

for i in range(1, number + 1):
    string_number = str(i)
    sum = 0
    for j in string_number:
        sum += int(j)
    is_special = False
    if sum == 5 or sum == 7 or sum == 11:
        is_special = True

    print(f'{i} -> {is_special}')
