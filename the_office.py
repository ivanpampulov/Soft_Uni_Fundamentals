def employees_happiness():

    employees_happiness = list(map(int, input().split()))
    factor = int(input())

    employees_happiness = [x*factor for x in employees_happiness]
    average = sum(employees_happiness) / len(employees_happiness)
    happy = [i for i in employees_happiness if i>= average]

    message = 'happy' if len(happy) >= (len(employees_happiness)/2) else 'not happy'

    print(f'Score: {len(happy)}/{len(employees_happiness)}. Employees are {message}!')

employees_happiness()