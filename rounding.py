random_numbers_list = input().split()
int_numbers = []
final_list = []

def integers(list):
    for i in random_numbers_list:
        i = float(i)
        i = round(i)
        int_numbers.append(i)
    return int_numbers

# def rounds(list):
#     for k in int_numbers:
#         k = round(k)
#         final_list.append(k)
#     return final_list

print(integers(random_numbers_list))


