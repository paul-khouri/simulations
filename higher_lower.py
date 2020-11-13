import random

def get_list(a,b):
    temp=[]
    for i in range(a,b+1):
        temp.append(i)
    #random.shuffle(temp)
    return temp

def win_probability(dealer_card, player):
    list_greater = [i for i in player if i > dealer_card]
    probability = len(list_greater)/len(player)
    return probability

def run_game():
    dealer = get_list(1,13)
    player = get_list(1,13)
    dealer_points = 0
    player_points = 0
    probabilities_list =[]
    while len(dealer) >0:
        dealer_card = random.choice(dealer)
        player_card = random.choice(player)
        dealer.remove(dealer_card)
        dealer_message = "The dealer card is {}".format(dealer_card)
        player_message = "The player cards are {}".format(player)
        probability = win_probability(dealer_card, player)
        probabilities_list.append(probability)
        if probability > 0.9:
            bet_value = 10
        elif probability > 0.5:
            bet_value = 5
        else:
            bet_value = 1
        win_prob = "The probability of a win is {}".format(probability)
        print(dealer_message)
        print(player_message)
        print(win_prob)
        player_message = "The player card is {}".format(player_card)
        print(player_message)
        player.remove(player_card)
        if dealer_card > player_card:
            dealer_points += bet_value
            player_points -= bet_value
            print("Dealer wins")
        elif dealer_card < player_card:
            player_points += bet_value
            dealer_points -= bet_value
            print("Player wins")
        else:
            print("Tie")
    print(player_points)
    print(dealer_points)
    return {"Player points": player_points , "Dealer Points": dealer_points, "Probabilities": probabilities_list}



def main():
    game_data = run_game()
    #print(game_data)
    print(sum(game_data["Probabilities"])/len(game_data["Probabilities"]))



if __name__ == "__main__":
    main()