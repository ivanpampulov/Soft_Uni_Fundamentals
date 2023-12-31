#User input

num = float(input())

if num == 0:
    print('zero')

if num > 0:
    if 1 < num < 1000000:
        print('positive')
    elif 0 < num < 1:
        print('small positive')
    else:
        print('large positive')

if num < 0:
    if -1 > num > -1000000:
        print('negative')
    elif 0 > num > -1:
        print('small negative')
    else:
        print('large negative')
