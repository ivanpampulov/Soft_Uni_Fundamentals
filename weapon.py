class Weapon:

    bullets = 0

    def __init__(self, bullets):
        self.bullets = bullets

    def __repr__(self):
        return f'Remaining bullets: {self.bullets - Weapon.bullets}'

    def shoot(self):
        if self.bullets > Weapon.bullets:
            print_str = 'shooting...'
            Weapon.bullets +=1

        else:
            print_str = 'no bullets left'

        return print_str

#Test code
weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)



