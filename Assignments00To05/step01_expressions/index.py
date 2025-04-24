#05_remainder_division
def main():
  print("remainder_division")
divide1 : int = int(input("enter an integer to be divided:  "))
divide2 : int = int(input("enter an integer to divide by:  "))
total: int = int(divide1//divide2 )
remainder: int = divide1 %divide2
print(f"the result of this division is {total} and the remainder is {remainder}")

if __name__ == '__main__':
    main()