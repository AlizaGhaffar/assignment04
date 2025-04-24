def get_first_element(lst):
   
    print("First element in the list is:", lst[0])

def get_lst():
    lst = []
   
    elem = input("Enter an element (press enter to stop): ")
       
    while elem != "":
        lst.append(elem)  
        elem = input("Enter an element (press enter to stop): ")  
    
    return lst  

def main():
    lst = get_lst()              
    get_first_element(lst)       

if __name__ == '__main__':
    main()



