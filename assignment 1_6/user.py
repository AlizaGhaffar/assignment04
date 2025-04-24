import random

def main():
    print("Think of a number between 1 and 100.")

    low = 1
    high = 100
    feedback = ""
    while  feedback != "c":
      guess = random.randint(low, high)
      print(f" my guess is: {guess}")
      feedback = input("it is (h), (l)ow or (c)orrect: ").lower()

      if feedback == "h":
            high = guess-1
      elif feedback == "l":
            low = guess+ 1

    print(f"Yay! I guessed your number: {guess} 🎉")

if __name__ == '__main__':
    main()
    
