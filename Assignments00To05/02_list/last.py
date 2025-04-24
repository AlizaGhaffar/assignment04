def get_last_element(lst):
    print("last element in the list is:",lst[-1])

def get_last():
    lst = []
    element = input("Enter an element (press enter to stop): ")
    while element != "":
        lst.append(element)
        element = input("Enter an element (press enter to stop): ")
    return lst
def main():
    lst = get_last()
    get_last_element(lst)

if __name__ == '__main__':
    main()



