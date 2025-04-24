
def add_three_copies(my_list, data):
        for i in range(3):
            my_list.append(data)
def main():
    message = input("enter a message to copy : ")
    my_list = []
    print("list_before", my_list)
    add_three_copies(my_list,message)
    print("list_after :" , my_list)



if __name__ == '__main__':
    main()