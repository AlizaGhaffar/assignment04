def main():
    lst = []
    value1 = input("enter a value")
    while value1:
        lst.append(value1)
        value1 = input("enter a value")
    print("here's the list:", lst)


if __name__ == '__main__':
    main()

