# list = input().split()
# list_int = []
#
# for i in list:
#     i = float(i)
#     i = abs(i)
#     list_int.append(i)
#
# print(list_int)
list = input().split()
list_as_float = []

def list_to_float(parameter):
    for i in list:
        i = float(i)
        i = abs(i)
        list_as_float.append(i)
        return

print(list_to_float(list))
