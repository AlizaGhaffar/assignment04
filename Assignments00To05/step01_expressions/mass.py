def main():
    mass = float(input("enter kilos of mass : "))
    
    print(f" m = {mass} kg")
    c = 299792458 
    E = mass * c**2
    print(f" energy = {E}")
if __name__ == '__main__':
    main()