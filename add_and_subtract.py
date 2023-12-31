num1 = int(input())
num2 = int(input())
num3 = int(input())

def sum_numbers(a, b):
    sum = a + b
    return sum

def subtract(sum, c):
    sub = sum - c
    return sub

print(subtract(sum_numbers(num1, num2), num3))