rooms = int(input())
total_people = 0
total_chairs = 0

for i in range(rooms):
    my_list = input().split()

    chairs = my_list[0].count('X')
    people = int(my_list[1])

    total_people += people
    total_chairs += chairs

    if people > chairs:
        print(f'{people-chairs} more chairs needed in room {i+1}')

if total_chairs > total_people:
    print(f'Game On, {total_chairs-total_people} free chairs left')