def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * length + 2 * width
    return area, perimeter

area, perimeter = rectangle_properties(10, 20)
print(f"Area: {area} and Perimeter: {perimeter}")