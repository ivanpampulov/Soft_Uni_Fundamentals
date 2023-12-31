def add_stop(index, old_string):
    result = old_string
    index = int(index)
    if 0 <= index < len(travel):
        result = old_string[:index] + new_string + old_string[index:]
    return result

def remove_stop(start_index, end_index, string):
    result = string
    start_index, end_index = int(start_index), int(end_index)

    if 0 <= start_index < len(travel) and 0<=end_index<len(travel):
        result = string[:start_index+1] + string[end_index:]
    return result

def switch(old_string, new_string, string):
    result = string

    if old_string in string:
        new_string = travel.replace(old_string, new_string)

    return string

travel = input()

while True:
    command = input()

    if command == 'Travel':
        break

    else:
        command_list = command.split(':')

    if command_list[0] == 'Add Stop':
        print(add_stop(command_list[1], command_list[2]))



