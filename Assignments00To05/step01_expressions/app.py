#04_pythagorean_theorem
import math
def main():
    print("pythagorean_theorem")
AB = float(input("Enter the length of AB: "))
AC = float(input("Enter the length of AC: "))
BC : float = math.sqrt( AB ** 2 + AC ** 2)
 

print(f"the length of BC(hypotenuse) is: {BC}  ")

if __name__ == '__main__':
    main()