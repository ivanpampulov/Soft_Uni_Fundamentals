my_list = list(map(int, input().split(', ')))
new_list = []
current_group = 10

while my_list:

    new_list = [x for x in my_list if x <= current_group]
    print(f"Group of {current_group}'s: {new_list}")

    for i in new_list:
        my_list.remove(i)

    current_group += 10


