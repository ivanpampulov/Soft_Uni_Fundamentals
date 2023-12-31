words = input().split()
words = [word for word in words if len(word) % 2 == 0]
print(*words, sep='\n')