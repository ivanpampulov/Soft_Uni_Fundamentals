sequence = input().split()
left_car_total = []
right_car_total = []
left_car = 0
right_car = 0

def str_to_list(list):
    int_list = [int(x) for x in list]
    return int_list

def middle_point(list):
    middle = len(list) // 2
    return middle

int_sequence = str_to_list(sequence)

for i in range(len(int_sequence)):

    middle = middle_point(int_sequence)
    left_car_total = int_sequence[:middle]
    right_car_total = int_sequence[1 + middle:]

for j in range(middle):
    if left_car_total[j] == 0:
        left_car = left_car * 0.8
    if right_car_total[middle -1 - j] == 0:
        right_car = right_car * 0.8

    left_car += left_car_total[j]
    right_car += right_car_total[middle -1 - j]

if left_car < right_car:
    print(f'The winner is left with total time: {left_car:.1f}')

else:
    print(f'The winner is right with total time: {right_car:.1f}')