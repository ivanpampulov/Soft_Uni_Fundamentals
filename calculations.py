operation = input()
num1 =  int(input())
num2 = int(input())


def mathematics(op, a, b):
    result = None
    if operation == 'multiply':
        result = int(a * b)
    elif operation == 'divide':
        if b == 0:
            print('Dividing by zero not possible!')
            quit()
        result = int(a / b)

    elif operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b

    return result

print(mathematics(operation, num1, num2))
