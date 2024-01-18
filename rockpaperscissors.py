import random
print("Welcome to rock, paper, scissors, lizard, spock! You will be playing against an automated opponent.")
print("--------------------")
player1=input("Player 1, would you like to choose rock, paper, scissors, lizard, or spock? ")
#player2=input("Player 2, would you like to choose rock, paper, scissors, lizard, or spock? ")
list = ["rock","paper","scissors","lizard","spock"]
player2 = random.choice(list)

print("Player 2 has chosen "+str(player2)+".")
print("----GAME RESULTS----")

#only rock paper scissors
# if player1=="rock" and player2=="rock":
#     print("Tie!")
# elif player1=="rock" and player2=="scissors":
#     print("Player 1 wins!")
# elif player1=="rock" and player2=="paper":
#     print("Player 2 wins!")
# elif player1=="paper" and player2=="paper":
#     print("Tie!")
# elif player1=="paper" and player2=="rock":
#     print("Player 1 wins!")
# elif player1=="paper" and player2=="scissors":
#     print("Player 2 wins!")
# elif player1=="scissors" and player2=="scissors":
#     print("Tie!")
# elif player1=="scissors" and player2=="paper":
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")

#+spock and lizard    
if player1=="rock" and player2=="rock":
    print("Tie!")
elif player1=="rock" and player2=="scissors":
    print("Player 1 wins!")
elif player1=="rock" and player2=="paper":
    print("Player 2 wins!")
elif player1=="rock" and player2=="lizard":
    print("Player 1 wins!")
elif player1=="rock" and player2=="spock":
    print("Player 2 wins!")

elif player1=="paper" and player2=="paper":
    print("Tie!")
elif player1=="paper" and player2=="rock":
    print("Player 1 wins!")
elif player1=="paper" and player2=="scissors":
    print("Player 2 wins!")
elif player1=="paper" and player2=="lizard":
    print("Player 2 wins!")
elif player1=="paper" and player2=="spock":
    print("Player 1 wins!")

elif player1=="scissors" and player2=="scissors":
    print("Tie!")
elif player1=="scissors" and player2=="paper":
    print("Player 1 wins!")
elif player1=="scissors" and player2=="rock":
    print("Player 2 wins!")
elif player1=="scissors" and player2=="lizard":
    print("Player 1 wins!")
elif player1=="scissors" and player2=="spock":
    print("Player 2 wins!")

elif player1=="lizard" and player2=="lizard":
    print("Tie!")
elif player1=="lizard" and player2=="rock":
    print("Player 2 wins!")
elif player1=="lizard" and player2=="paper":
    print("Player 1 wins!")
elif player1=="lizard" and player2=="scissors":
    print("Player 2 wins!")
elif player1=="lizard" and player2=="spock":
    print("Player 1 wins!")
    
elif player1=="spock" and player2=="spock":
    print("Tie!")
elif player1=="spock" and player2=="rock":
    print("Player 1 wins!")
elif player1=="spock" and player2=="paper":
    print("Player 2 wins!")
elif player1=="spock" and player2=="scissors":
    print("Player 1 wins!")
elif player1=="spock" and player2=="lizard":
    print("Player 2 wins!")
else:
    print("Please only choose 'rock', 'paper', 'scissors', 'lizard', or 'spock'.")