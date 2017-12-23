# ---- START FUNCTIONS ---- #


# passing all 6 lists in to function via list_of_lists
def pile_choice(list_of_lists):
    print(user_choice)
# Filling empty lists, with list items from pile_1,2 and 3, based on user input
    if user_choice == 1:
        list_of_lists[3] = list_of_lists[0].copy()
        list_of_lists[4] = list_of_lists[1].copy()
        list_of_lists[5] = list_of_lists[2].copy()
    elif user_choice == 2:
        list_of_lists[3] = list_of_lists[1].copy()
        list_of_lists[4] = list_of_lists[0].copy()
        list_of_lists[5] = list_of_lists[2].copy()
    elif user_choice == 3:
        list_of_lists[3] = list_of_lists[2].copy()
        list_of_lists[4] = list_of_lists[1].copy()
        list_of_lists[5] = list_of_lists[0].copy()
    return list_of_lists


# Values from previous func passed into this function
def deal_cards(list_of_lists):  # Responsible for shuffling cards.
# indexes of pile_1,2,3 equal to specific indexes of middle, top & bottom
    list_of_lists[0][0] = list_of_lists[4][0]
    list_of_lists[0][1] = list_of_lists[4][3]  # e.g pile_1[1] = middle_pile[3]
    list_of_lists[0][2] = list_of_lists[4][6]
    list_of_lists[0][3] = list_of_lists[3][2]
    list_of_lists[0][4] = list_of_lists[3][5]
    list_of_lists[0][5] = list_of_lists[5][5]
    list_of_lists[0][6] = list_of_lists[5][6]

    list_of_lists[1][0] = list_of_lists[4][1]
    list_of_lists[1][1] = list_of_lists[4][4]
    list_of_lists[1][2] = list_of_lists[3][0]
    list_of_lists[1][3] = list_of_lists[3][3]
    list_of_lists[1][4] = list_of_lists[3][6]
    list_of_lists[1][5] = list_of_lists[5][2]
    list_of_lists[1][6] = list_of_lists[5][5]

    list_of_lists[2][0] = list_of_lists[4][2]
    list_of_lists[2][1] = list_of_lists[4][5]
    list_of_lists[2][2] = list_of_lists[3][1]
    list_of_lists[2][3] = list_of_lists[3][4]
    list_of_lists[2][4] = list_of_lists[5][0]
    list_of_lists[2][5] = list_of_lists[5][3]
    list_of_lists[2][6] = list_of_lists[5][6]
    return list_of_lists


# Prints index 0, 1 and 2 of list_of_lists (pile_1,2&3)
def print_piles(list_of_lists):
    for x in range(0, 3):
        print('Pile', x + 1, ': ', list_of_lists[x], "\n")
    return list_of_lists


# ---- END FUNCTIONS ---- #

# ---- START VARIABLES ---- #
pile_1 = ['9 of Spades', '4 of Spades', 'Jack of Spades', '8 of Spades',
          '7 of Diamonds', 'Ace of Diamonds', '10 of Diamonds']
pile_2 = ['5 of Diamonds', '10 of Spades', '3 of Spades', '6 of Spades',
          '9 of Diamonds', '7 of Spades', '2 of Spades']
pile_3 = ['5 of Spades', '4 of Diamonds', '6 of Diamonds', 'Queen of Spades',
          '3 of Diamonds', 'King of Spades', 'Queen of Diamonds']
middle_pile = []
top_pile = []
bottom_pile = []
list_of_lists = [pile_1, pile_2, pile_3, middle_pile, top_pile, bottom_pile]
valid = [1, 2, 3]
play_again_valid = [0, 1]
user_choice = None
first_choice = 0
play_again = None
iterations = 0
# ---- END OF VARIABLES ---- #

while True:
    # Infinite loop. Allows user to play again. Will break when play_again = 1

    first_choice = 0
    play_again = None
    iterations = 0
    # Resetting variables from previous turn for every iteration of while loop

    print_piles(list_of_lists)

    for i in range(0, 3):  # executes the functions 3 times.
        iterations += 1  # add 1 to value for every iteration of the for loop.

        if first_choice == 0:
        # validating user input
            while user_choice not in valid:
                user_choice = int(input("Choose a card and enter the " +
                                        "pile it appears in (1, 2 or 3):"))
                first_choice += 1
        else:
            while user_choice not in valid:
                user_choice = int(input("Input the pile your card " +
                                        "now appears in (1, 2 or 3): "))

        pile_choice(list_of_lists)  # Fill empty lists via function
        deal_cards(list_of_lists)  # Rearranging indexes of lists via function

    # Only print the shuffled piles for the first 2 iterations of the For loop
        if iterations < 3:
            print_piles(list_of_lists)

        user_choice = None

    print("Your card is the", list_of_lists[3][3])

    while play_again not in play_again_valid:
        play_again = int(input("Enter 0 to play again " +
                               "or 1 to exit the game: "))

    if play_again == 1:
        break
    else:
        print("Have another go: ")
print("Thank you for playing!")
