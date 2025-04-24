import random
def main():
    print("guess my number")
    secret_num :int = random.randint(1, 99)
    print("I am thinking of a number between 0 and 99")

    guess = int(input("enter a guess: "))

    while guess != secret_num :
        if guess< secret_num:
            print("your guess is too low")
        else: 
            print("your guess is too high")
            
        guess = int(input("enter a guess: "))
    print("congrats! your guess is corrected its", secret_num)


if __name__ == '__main__':
    main()