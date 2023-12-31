# Function to perform a single faro shuffle on the deck
def faro_shuffle(deck):
    middle = len(deck) // 2
    first_half = deck[:middle]
    second_half = deck[middle:]
    shuffled_deck = []

    for i in range(middle):
        shuffled_deck.append(first_half[i])
        shuffled_deck.append(second_half[i])

    return shuffled_deck

# Input: Read the deck and the number of faro shuffles
initial_deck = input().split()
num_shuffles = int(input())

# Perform the specified number of faro shuffles
for _ in range(num_shuffles):
    initial_deck = faro_shuffle(initial_deck)

# Output: Print the state of the deck after shuffling
print("The state of the deck after", num_shuffles, "faro shuffle(s):")
print(" ".join(initial_deck))