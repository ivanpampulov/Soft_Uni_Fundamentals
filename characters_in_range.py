char1 = ord(input())
char2 = ord(input())
counter = char2 - char1

for _ in range(1, counter):
    char1 += 1
    print(chr(char1), end=' ')



