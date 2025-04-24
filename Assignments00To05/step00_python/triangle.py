def main():
    print("triangle_perimeter")
    one_side: int= input("enter the length of one side of triangle : ")
    second_side:int= input("length of 2nd side : ")
    third_side :int=input("length of 3rd side : ")
    total_length = one_side + second_side + third_side
    print(f" The perimeter of the triangle is : {total_length} ")

if __name__ == '__main__':
    main()