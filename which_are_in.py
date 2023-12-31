def sequence():
    sequence_list = input().split(', ')
    my_list = input().split(', ')
    final_list = []

    for i in sequence_list:
        for j in my_list:
            if i in j:
                final_list.append(i)
                break

    return final_list

print('.'.join(map(str, sequence())))
