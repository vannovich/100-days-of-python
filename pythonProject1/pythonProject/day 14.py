from getpass import getpass as input
print("E P I C ROCK, PAPER, SCISSORS GAME B A T T L E")
print("Select your move (Rock, Paper or Scissors)")
player1 = input("Player1 select your move: ")
player2 = input("Player2 select your move: ")
if (player1 == "Rock" or player1 == "rock") and (player2 == "Paper" or player2 == "paper"):
    print("Player1's rock is smothered by player2's paper!")
elif (player1 == "Paper" or player1 == "paper") and (player2 == "Rock" or player2 == "rock"):
    print("Player2's rock is smothered by player1's paper!")
elif (player1 == "Paper" or player1 == "paper") and (player2 == "Scissors" or player2 == "scissors"):
    print("Player1's paper is choped by player2's scissors!")
elif (player1 == "Scissors" or player1 == "scissors") and (player2 == "paper" or player2 == "Paper"):
    print("Player2's paper is choped by player1's scissors!")
else:
    print("Restart Game!!!")


