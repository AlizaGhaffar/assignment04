def main():
    year : int = int (input("enter a year: "))
    
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
                print("thats a leap year")
            else:
                print("thats not a leap year")
        else:
           print("thats a leap year")
    else:
        print("thats not a leap year")

if __name__ == '__main__':
    main()