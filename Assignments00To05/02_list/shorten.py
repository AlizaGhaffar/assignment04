MAX_LENGTH = 3
def shorten(lst):
    while len(lst)> MAX_LENGTH:
        last_element = lst.pop()
        print(last_element)

def get_lst():
    lst = []
    elem = input("enter element and to stop this press enter: ")
    while elem != "":
        lst.append(elem)
        elem = input("enter element and to stop this press enter: ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()

