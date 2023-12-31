num1 = int(input())
num2 = int(input())
num3 = int(input())

list = [num1, num2, num3]

def smallest(list):
    smallest_number = min(list)
    return smallest_number

print(smallest(list))