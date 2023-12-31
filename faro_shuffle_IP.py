deck = input().split()

num_shuffles = int(input())

#Logic

for i in range(num_shuffles):
    middle = len(deck) // 2
    firs_half = deck[:middle]
    second_half = deck[middle:]
    shuffled_deck = []

    for j in range(middle):
        shuffled_deck.append(firs_half[j])
        shuffled_deck.append(second_half[j])
        deck = shuffled_deck

print(deck)