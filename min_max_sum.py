my_list = input().split()

def str_to_int(list):
    int_list = [int(x) for x in list]
    return int_list

print(f'The minimum number is {min(str_to_int(my_list))}')
print(f'The maximum number is {max(str_to_int(my_list))}')
print(f'The sum number is: {sum(str_to_int(my_list))}')