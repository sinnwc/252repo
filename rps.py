player_one = input("Player one, make your selection: ") # p1 input
print("NO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\nNO CHEATING!\n")
player_two = input("Player two, make your selection: ") #p1 input
print("Shoot!")

if player_one == "rock" or player_one == "Rock":
    player_one = 1  # converts multiple possible inputs to int value
elif player_one == "paper" or player_one == "Paper":
    player_one = 2  # converts multiple possible inputs to int value
elif player_one == "scissors" or player_one == "Scissors":
    player_one = 3  # converts multiple possible inputs to int value
else:
    player_one = 0
    print("Player one, you didn't enter a valid hand.") # displayed if p2 does not submit a valid hand

if player_two == "rock" or player_one == "Rock":
        player_two = 1  # converts multiple possible inputs to int value
elif player_two == "paper" or player_one == "Paper":
        player_two = 2  # converts multiple possible inputs to int value
elif player_two == "scissors" or player_one == "Scissors":
        player_two = 3  # converts multiple possible inputs to int value
else:
        player_two = 0
        print("Player two, you didn't enter a valid hand.") # displayed if p2 does not submit a valid hand

if player_one == player_two:
    print("Draw!") # draw, self-explanatory
elif player_one == 0 or player_two == 0:
    print("Restart the round.") # if input of either player is null, game ends
    
else:
    if player_one == 2 and player_two == 1: # p1 wins w/ paper
        print("Player one wins!")
    elif player_one == 3 and player_two == 2: #p1 wins w/ scissors
        print("Player one wins!")
    elif player_one == 1 and player_two == 3: #p1 wins w/ rock
        print("Player one wins!")
    else:
        print("Player two wins!") # p2 will win every other case.