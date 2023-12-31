factor = int(input())
counter = int(input())
my_list = []
new_number = 0

for i in range(counter):
    new_number += factor
    my_list.append(new_number)

print(my_list)