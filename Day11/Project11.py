"Day10"

print("THE BLACKJACK CAPSTONE PROJECT")

logo = """
┌───────────────┐
│   BLACKJACK   │
│    ♠ ♥ ♦ ♣    │
│    21 GAME    │
└───────────────┘
"""
print(logo)

def calculate_score(score):
    total = sum(score)
    while total > 21 and 11 in score:
        score[score.index(11)] = 1
        total = sum(score)
    return total

cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]


import random
condition=True
while condition:
    
    user_choice = random.choices(cards, k=2)
    dealer_choice = random.choices(cards, k=2)

    user_score = calculate_score(user_choice)
    dealer_score = calculate_score(dealer_choice)

    print(f"Your cards: {user_choice}, current score = {user_score}")
    print(f"Dealer's first card: {dealer_choice[0]}")


    while user_score < 21:
        game_continue = input("Type 'y' to get another card, type 'n' to pass: ")

        if game_continue == "y":
            user_choice.append(random.choice(cards))
            user_score = calculate_score(user_choice)
            print(f"Your cards: {user_choice}, current score = {user_score}")
        else:
            break


    while dealer_score < 17 and user_score <= 21:
        dealer_choice.append(random.choice(cards))
        dealer_score = calculate_score(dealer_choice)

    print(f"Dealer's final cards: {dealer_choice}, final score = {dealer_score}")


    if user_score > 21:
        print("You went over. You lose")
    elif dealer_score > 21:
        print("Dealer went over. You win!")
    elif user_score == dealer_score:
        print("Draw")
    elif user_score > dealer_score:
        print("You win!")
    else:
        print("You lose")

    replay=input("Do you want to play again? yes/no: ").lower()
    if replay=="yes":
        condition=True
    elif replay=="no":
        print("Thanks for playing!")
        condition=False
    