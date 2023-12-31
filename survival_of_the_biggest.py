list_string = input().split(' ')
list_numbers = []
final_list_string = []
counter = int(input())

#logic
for i in list_string:
    list_numbers.append(int(i))

for j in range(counter):
    n = min(list_numbers)
    list_numbers.remove(n)

for k in list_numbers:
    final_list_string.append(str(k))

glue = ', '
s = glue.join(final_list_string)

print(s)