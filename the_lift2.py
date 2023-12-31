que_line = int(input())
wagoons = input().split()
people_on_lift = []

def str_to_int(list):
    int_str = [int(x) for x in list]
    return int_str

int_str = str_to_int(wagoons)

for i in int_str:
    free_spaces = 4 - i

    if que_line <= free_spaces:
        people_on_lift.append(i + que_line)
        que_line = 0
        break

    que_line -= free_spaces
    people_on_lift.append(free_spaces + i)

if que_line == 0 and sum(people_on_lift) < len(int_str) * 4:
    print('The lift has empty spots!')

if que_line > 0:
    print(f"There isn't enough space! {que_line} people in a queue!")

for j in people_on_lift:
    print(j, end=" ")