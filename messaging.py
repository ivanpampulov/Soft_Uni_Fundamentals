numbers = input().split()
input_string = input()
final_message = ''
index = 0
index_list = []

for i in numbers:
    for k in i:
        index += int(k)
    index_list.append(index)
    index = 0
#
for k in range(len(index_list)):
    index = index_list[k] + k
    if index >= len(input_string):
        take = index - len(input_string)
        final_message += input_string[take]

    else:
        final_message += input_string[index]

print(final_message)

