number_of_electrons = int(input())
n = 1
my_list = []

while True:
    shell = 2 * (n**2)

    if number_of_electrons <2:
        my_list.append(n)
        break

    if number_of_electrons <= shell:
        my_list.append(number_of_electrons)
        break

    number_of_electrons -= shell

    my_list.append(shell)
    n += 1

    if number_of_electrons == 0:
        break



print(my_list)


