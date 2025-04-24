#temperature converter
def main():
    print("fahrenheit_to_celsius")
    temp = float(input("enter temperature in fahrenheit : "))
    temp_converter = (temp - 32) * 5.0/9.0
    print(f"the temperature in celsius is : {temp_converter}")

if __name__ == '__main__':
    main()

