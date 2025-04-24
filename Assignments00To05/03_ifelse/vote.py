PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48
def main():
    age :int = int(input("enter your age: "))

    if age >= PETURKSBOUIPO_AGE:
        print("you are eligible in PETURKSBOUIPO_AGE for vote where the voting age is ",PETURKSBOUIPO_AGE)
    else:
        print("You cannot vote in Peturksbouipo where the voting age is",PETURKSBOUIPO_AGE)

    if age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is ",STANLAU_AGE)
    else:
        print("You cannot vote in Stanlau where the voting age is ",STANLAU_AGE)
    
    
    if age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is ",MAYENGUA_AGE)
    else:
        print("You cannot vote in Mayengua where the voting age is ",MAYENGUA_AGE)

if __name__ == '__main__':
    main()