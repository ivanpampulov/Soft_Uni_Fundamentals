#Read user input

divisor = int(input())
boundary = int(input())
largest = 0

#logic
for i in range(boundary+1):
    if i % divisor == 0 and 0 < i <= boundary:
        largest = i

print(largest)

