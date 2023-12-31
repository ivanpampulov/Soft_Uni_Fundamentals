
#User input

string1 = input()
string2 = input()
last_str = string1

#Logic
for i in range(len(string1)):
    left_part = string2[:i+1]
    right_part = string1[i+1:]
    new_string = left_part + right_part

    if last_str == new_string:
        continue

    last_str = new_string
    print(new_string)