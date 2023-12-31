number_heroes = int(input())
heroes_dict = {}

for i in range(number_heroes):
    name, hit, mana = input().split()
    heroes_dict[name] = [int(hit), int(mana)]
    if heroes_dict[name][0] > 100:
        heroes_dict[name][0] = 100

    if heroes_dict[name][1] > 200:
        heroes_dict[name][1] = 200

while True:
    command = input()

    if command == 'End':
        break

    if command.startswith('CastSpell'):
        do, name, mana, spell = command.split(' - ')
        mana = int(mana)

        if heroes_dict[name][1] >= mana:
            heroes_dict[name][1] -= mana
            print(f'{name} has successfully cast {spell} and now has {heroes_dict[name][1]} MP!')
        else:
            print(f'{name} does not have enough MP to cast {spell}!')

    if command.startswith('TakeDamage'):
        do, name, damage, attacker = command.split(' - ')
        damage = int(damage)
        heroes_dict[name][0] -= damage

        if heroes_dict[name][0] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_dict[name][0]} HP left!")
        else:
            print(f'{name} has been killed by {attacker}!')

    if command.startswith('Recharge'):
        do, name, mana = command.split(' - ')
        mana = int(mana)
        maximum = 200 - heroes_dict[name][1]
        heroes_dict[name][1] += mana

        if heroes_dict[name][1] > 200:
            heroes_dict[name][1] = 200
            print(f'{name} recharged for {maximum} MP!')
        else:
            print(f'{name} recharged for {mana} MP!')

    if command.startswith('Heal'):
        do, name, hit = command.split(' - ')
        hit = int(hit)
        maximum = 100 - heroes_dict[name][0]
        heroes_dict[name][0] += hit

        if heroes_dict[name][0] > 100:
            heroes_dict[name][0] = 100
            print(f'{name} healed for {maximum} HP!')
        else:
            print(f'{name} healed for {hit} HP!')

for name, status in heroes_dict.items():
    if status[0] > 0:
        print(f'{name}')
        print(f'  HP: {status[0]}')
        print(f'  MP: {status[1]}')
    else:
        pass

