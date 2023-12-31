string = input()
my_list = string.split(' ')
new_list = []

for i in my_list:
    i = int(i)
    new_number = i * (-1)
    new_list.append(new_number)

print(new_list)

