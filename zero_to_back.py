list = input().split(', ')

def str_to_int(list):
    int_list = [int(x) for x in list]
    return int_list

list = str_to_int(list)

for i in list:
    if list[i] == 0:
        list.remove(i)
        list = list[:] + i

print(list)