text = input().split()
final_string = ''

for i in text:
    for_print = i * len(i)
    final_string += for_print

print(final_string)