import random

while (True):
  print("\n --- Rock-Paper Game ---- \n    Let's play")
  print(
    "\n Enter your choice : \n 1 for Rock \n 2 for Paper \n 3 for Scissor \n ")
  player_choice = int(input(" Your choice: "))

  while (player_choice > 3 or player_choice < 1):
    print("\n Oops! It's an invalid choice")
    player_choice = int(input("\n Enter a valid choice : "))
  if (player_choice == 1):
    player = "rock"
  elif (player_choice == 2):
    player = "paper"
  else:
    player = "scissor"

  computer_choice = random.randint(1, 3)

  if computer_choice == 1:
    computer = "rock"
  elif computer_choice == 2:
    computer = "paper"
  else:
    computer = "scissor"

  print("\n You chose", player, "Computer chose", computer)

  if player_choice == computer_choice:
    print("\n Oh!! It's a tie")
  elif player_choice == 1:
    if computer_choice == 2:
      print(
        "\n Paper covered the Rock..... \n Ohh!! You lose... Better Luck next time!"
      )
    else:
      print("\n Rock smashed the scissor.... \n Hey!! You won... Congrats!!")
  elif player_choice == 2:
    if computer_choice == 1:
      print("\n Paper covered the Rock..... \n Hey!! You won.. Congrats!!")
    else:
      print(
        "\n Scissor cut the Paper.... \n Ohh!! You lose... Better Luck next time!"
      )
  elif player_choice == 3:
    if computer_choice == 1:
      print(
        "\n Rock smashed the scissor.... \n Ohh!! You lose... Better Luck next time"
      )
    else:
      print("\n Scissor cut the papaer.... \n Hey!! You won... Congrats!!")

  print("\n Wanna play it again ?   ")
  option = input("\n Press y for Yes or n for No : ")

  if option == 'n':
    print("\n Thanks for playing \n Have a good day!! \n ")
    break
  elif option == 'y':
    continue
  else:
    print("--------Wrong input. Sorry!----------")
    break
