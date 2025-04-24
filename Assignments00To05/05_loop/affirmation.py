AFFIRMATION =  "I am capable of doing anything I put my mind to"
def main():
    print("Please type the following affirmation: " ,AFFIRMATION)
    user = input()

    while user != AFFIRMATION:
        print("That was not the affirmation.")
        print("plz type the correct  affirmation", AFFIRMATION)
        user = input()
    print("thats right boss!")

if __name__ == '__main__':
    main()