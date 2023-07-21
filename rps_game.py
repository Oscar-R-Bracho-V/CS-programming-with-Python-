import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock, Scissors, and Paper game!")
print("*" * 46)
game_img = [rock, scissors, paper]

player_choice = input("Choose your move (0 for rock, 1 for scissors, or 2 for paper): ")
try:
    player_choice = int(player_choice)
    if player_choice < 0 or player_choice >= len(game_img):
        print("Invalid move. Please choose a valid option.")
    else:
        print(f"\nPlayer's move:\n {game_img[player_choice]}")

        computer_choice = random.randint(0, 2)
        print(f"Computer's move:\n {game_img[computer_choice]}\n")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == 0:
            if computer_choice == 1:
                print("Player wins! Rock smashes scissors.")
            else:
                print("Computer wins! Paper covers rock.")
        elif player_choice == 1:
            if computer_choice == 2:
                print("Player wins! Scissors cuts paper.")
            else:
                print("Computer wins! Rock smashes scissors.")
        elif player_choice == 2:
            if computer_choice == 0:
                print("Player wins! Paper covers rock.")
            else:
                print("Computer wins! Scissors cuts paper.")
except ValueError:
    print("Invalid input. Please enter a valid number.")