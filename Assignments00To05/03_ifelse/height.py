MINIMUM_HEIGHT : int = 50
def main():
    height: float = float(input("How tall are you in inches"))
    if height >= MINIMUM_HEIGHT:
        print("you are eligible")
    else:
        print("you are not taller enough drink complan")

if __name__ == '__main__':
    main()