def main():
    print("Welcome to Mad Libs!")
    adjective = input("enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")

    story = f""" 
         one day a {adjective} went to a park with {noun} they {verb} and after 
         that they went to {place} """
    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == '__main__':
    main()