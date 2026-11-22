from shape import Shape
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from square import Square

def main():
    # TODO: build a list holding a mix of superclass/subclass instances --
    #       this is the "collection data structure" the Common Requirement
    #       asks for.
    shapes = [
        Circle("circle1", 3),
        Rectangle("rect1", 4, 5),
        Triangle("tri1", 3, 4),
        Square("square1", 4)
    ]

    print("Areas of various shapes:")
    for shape in shapes:  # polymorphism: each shape computes its own area
        print(f"{shape.__class__.__name__} area: {shape.area():.2f}")


if __name__ == "__main__":
    main()
