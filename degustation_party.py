liked_dict = {}
disliked_dict = {}
disliked_meals = []

while True:
    command = input()

    if command == "Stop":
        break

    action, name, meal = command.split('-')

    if action == 'Like':
        if name not in liked_dict:
            liked_dict[name] = [meal]

        elif meal in liked_dict[name]:
            pass

        else:
            liked_dict[name] += [meal]

    if action == 'Dislike':
        if name not in liked_dict:
            print(f'{name} is not at the party.')
        elif meal not in liked_dict[name]:
            print(f'{name} doesn\'t have the {meal} in his/her collection.')
        else:
            liked_dict[name].remove(meal)
            disliked_meals.append(meal)
            print(f'{name} doesn\'t like the {meal}.')

for name, meals in liked_dict.items():
    print(f'{name}: {", ".join(meals)} ')
print(f'Unliked meals: {len(disliked_meals)}')