import math


def main_menu():
    print("""
1. Calculate Area
2. Calculate Perimeter
3. Calculate Volume
4. Exit
""")
    choice = int(input("Choose an operation: "))
    if choice == 1:
        area_menu()
    elif choice == 2:
        perimeter_menu()
    elif choice == 3:
        volume_menu()
    elif choice == 4:
        print("Exiting program.")
        exit()
    else:
        print("Invalid selection. Please try again.")
        main_menu()


def area_menu():
    print("""
1. Area Of Circle
2. Area Of Triangle
3. Area Of Rectangle
4. Area Of Isosceles Triangle
5. Area Of Parallelogram
6. Area Of Rhombus
7. Area Of Equilateral Triangle
""")
    choice = int(input("Select the figure: "))
    if choice == 1:
        Acircle()
    elif choice == 2:
        Atriangle()
    elif choice == 3:
        Arectangle()
    elif choice == 4:
        Aisosceles_triangle()
    elif choice == 5:
        Aparallelogram()
    elif choice == 6:
        Arhombus()
    elif choice == 7:
        Aequilateral_triangle()
    else:
        print("Invalid selection. Please try again.")
        area_menu()


def perimeter_menu():
    print("""
1. Perimeter Of Circle
2. Perimeter Of Equilateral Triangle
3. Perimeter Of Parallelogram
4. Perimeter Of Rectangle
5. Perimeter Of Square
6. Perimeter Of Rhombus
""")
    choice = int(input("Select the figure: "))
    if choice == 1:
        Pcircle()
    elif choice == 2:
        Pequilateral_triangle()
    elif choice == 3:
        Pparallelogram()
    elif choice == 4:
        Prectangle()
    elif choice == 5:
        Psquare()
    elif choice == 6:
        Prhombus()
    else:
        print("Invalid selection. Please try again.")
        perimeter_menu()


def volume_menu():
    print("""
1. Volume Of Cylinder
2. Volume Of Cone
3. Volume Of Sphere
""")
    choice = int(input("Select the solid: "))
    if choice == 1:
        Vcylinder()
    elif choice == 2:
        Vcone()
    elif choice == 3:
        Vsphere()
    else:
        print("Invalid selection. Please try again.")
        volume_menu()


def Acircle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"Area of circle: {area:.2f}")


def Atriangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"Area of triangle: {area:.2f}")


def Arectangle():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print(f"Area of rectangle: {area:.2f}")


def Aisosceles_triangle():
    base = float(input("Enter the base: "))
    side = float(input("Enter the side length: "))
    height = math.sqrt(side ** 2 - (base / 2) ** 2)
    area = (base * height) / 2
    print(f"Area of isosceles triangle: {area:.2f}")


def Aparallelogram():
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = base * height
    print(f"Area of parallelogram: {area:.2f}")


def Arhombus():
    diagonal1 = float(input("Enter the first diagonal: "))
    diagonal2 = float(input("Enter the second diagonal: "))
    area = (diagonal1 * diagonal2) / 2
    print(f"Area of rhombus: {area:.2f}")


def Aequilateral_triangle():
    side_length = float(input("Enter the side length: "))
    area = (math.sqrt(3) / 4) * side_length ** 2
    print(f"Area of equilateral triangle: {area:.2f}")


def Pcircle():
    radius = float(input("Enter the radius: "))
    circumference = 2 * math.pi * radius
    print(f"Circumference of circle: {circumference:.2f}")


def Pequilateral_triangle():
    side_length = float(input("Enter the side length: "))
    perimeter = 3 * side_length
    print(f"Perimeter of equilateral triangle: {perimeter:.2f}")


def Pparallelogram():
    side_a = float(input("Enter one side length: "))
    side_b = float(input("Enter the adjacent side length: "))
    perimeter = 2 * (side_a + side_b)
    print(f"Perimeter of parallelogram: {perimeter:.2f}")


def Prectangle():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    perimeter = 2 * (length + width)
    print(f"Perimeter of rectangle: {perimeter:.2f}")


def Psquare():
    side = float(input("Enter the side length: "))
    perimeter = 4 * side
    print(f"Perimeter of square: {perimeter:.2f}")


def Prhombus():
    side = float(input("Enter the side length: "))
    perimeter = 4 * side
    print(f"Perimeter of rhombus: {perimeter:.2f}")


def Vcylinder():
    radius = float(input("Enter the radius of the base: "))
    height = float(input("Enter the height: "))
    volume = math.pi * radius ** 2 * height
    print(f"Volume of cylinder: {volume:.2f}")


def Vcone():
    radius = float(input("Enter the radius of the base: "))
    height = float(input("Enter the height: "))
    volume = (math.pi * radius ** 2 * height) / 3
    print(f"Volume of cone: {volume:.2f}")


def Vsphere():
    radius = float(input("Enter the radius: "))
    volume = (4 / 3) * math.pi * radius ** 3
    print(f"Volume of sphere: {volume:.2f}")


if __name__ == "__main__":
    main_menu()
