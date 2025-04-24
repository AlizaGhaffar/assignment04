#Mad Libs game

def main():
    sentence_start = "Code in Place is fun. I learned to program and used Python to make my"
    adj = input("Enter an adjective: ")
    noun = input("Enter an noun: ")
    verb = input("Enter an verb: ")
    print(f"{sentence_start} {adj} {noun} {verb}")

if __name__ == '__main__':
    main()
