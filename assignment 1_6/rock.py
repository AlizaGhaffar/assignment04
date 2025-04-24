import random
def main():
 options= ["rock", "paper", "scissors"]

 user_choice = input("Choose rock, paper, or scissors: ").lower()
 computer_choice = random.choice(options)
 print(f"you choose {user_choice}")
 print(f"computer choose {computer_choice}")

 if user_choice == computer_choice:
  print("game draw")
 elif user_choice == "rock":
  if computer_choice == "scissors":
   print("you win")
  else:
     print("you lose")
 elif user_choice == "paper":
  if computer_choice == "rock":
   print("you win")
  else:
        print("You lose!")
 elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")
 else:
    print("Invalid choice!")

if __name__ == '__main__':
    main()