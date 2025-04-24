import random
def main():
    print(" wellcome to :) Guess the Number Game")
    value =random.randint(1, 99)
    secrete_num : int= int(input("enter a guess between 1 and 99: "))
    while value != secrete_num :
        if  secrete_num < value:
            print("your guess is low")
        else: 
            print("your guess is high")
        secrete_num = int(input("enter a guess between 1 and 99: "))
    print("congrats your guess is correct the value is: ", secrete_num)

if __name__ == '__main__':
    main()

