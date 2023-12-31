def loading_bar():
    percentage = int(input())
    the_bar = ['.'] *10

    if percentage == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
        quit()

    counter = int(percentage/10)

    for i in range(counter):
        the_bar.pop(i)
        the_bar.insert(i, '%')

    for_print = ''.join(the_bar)

    print(f'{percentage}% [{for_print}]')
    print('Still loading...')

    return

loading_bar()

