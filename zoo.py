class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)

        elif species == 'fish':
            self.fishes.append(name)

        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        string_for_print = ""
        if species == "mammal":
            string_for_print += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            string_for_print += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            string_for_print += f"Birds in {self.name}: {', '.join(self.birds)}"
        string_for_print += f"\nTotal animals: {Zoo.__animals}"
        return string_for_print

zoo_name = input()
zoo1 = Zoo(zoo_name)

counter = int(input())

for i in range(counter):
    species, name = input().split()
    zoo1.add_animals(species, name)

species = input()

print(zoo1.get_info(species))



