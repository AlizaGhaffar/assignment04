def main():
    current_value:int = int(input("enter a number: "))
    print(current_value)
    while current_value < 100:
        current_value = current_value * 2
        print(current_value)

if __name__ == '__main__':
    main()