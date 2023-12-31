my_list = input().split()

def string_to_int(string_list):
    int_list = [int(x) for x in string_list]
    return int_list

int_list = string_to_int(my_list)

print(sorted(int_list))