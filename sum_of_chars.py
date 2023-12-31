number_char = int(input())
total_ascii = 0

for i in range(number_char):
    char = input()

    total_ascii += ord(char)

print(f'The sum equals: {total_ascii}')