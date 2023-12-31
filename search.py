counter = int(input())
target = input()
list = []
filtered_list = []

for i in range(counter):
    string = input()

    list.append(string)

print(list)

for current_string in list:
    if target in current_string:
        filtered_list.append(current_string)

print(filtered_list)
