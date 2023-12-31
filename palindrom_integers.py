my_list = input().split(', ')
new_number = ''

for i in my_list:
    for j in i[::-1]:
        new_number += j

    if new_number == i:
        new_number = ''
        print(True)

    else:
        new_number = ''
        print(False)
