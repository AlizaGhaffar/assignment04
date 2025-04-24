import random
def main():
    print("guess my number")
    print("im thinking of a number between 0 and 99....")

    secrete_num = random.randint(0,99)
    guess: int= int(input("enter a guess: "))
    while guess != secrete_num:
        if guess< secrete_num :
            print("your guess is too loww")
        else:
            print("your guess is too high")
        print()
        guess: int= int(input("enter a guess: "))

    print("congrats your guess is correct queen the num was", secrete_num)

if __name__ == '__main__':
    main()