"""
-------------------------------------------------------------------------------
BRIDGE - Structural Pattern
-------------------------------------------------------------------------------

https://refactoring.guru/design-patterns/bridge

Bridge is a structural design pattern that lets you split a large class or a set
of closelu related classes into two separate hierarchies - abstraction and
implementation - which can be developed independently of each other.

Say you have a geometric "Shape" class with a pair of subclasses"
- "Circle" and "Square"

You want to extend this class hierarchy to incorporate colors, so you plan to
create"
- "Red" and "Blue" subclasses

However, since you already have two subclasses, you'll need to create four class
combinations such as:
- "BlueCircle", "BlueSquare", "RedCircle" and "RedSquare"

Adding a new shape type and color to the hierarchy, will grow it exponentially.
For example, to add a triangle shape you'll need to introduce two new subclasses
- "BlueTriangle", "RedTriangle"


SOLUTION
-------------------------------------------------------------------------------
The bridge pattern attempts to solve this problem by switching from inheritance
to object composition.

You extract one of the dimensions into a separate class hierarchy, so that the
original classes will reference an object of the new hierarchy, instead of
having all of its state and behaviors within one class.

Following this approach you can extract the color-related code into its own
class with two subclasses: "Red" and "Blue".

The "Shape" class then gets a reference field pointing to one of the color
objects. Now the shape can delegate any color-related work to the linked color
object


https://www.geeksforgeeks.org/bridge-method-python-design-patterns/
"""


class RedShape:
    def generate_shape(self, nr_sides, shape_str):
        print(f"Generating a red {shape_str} with {nr_sides} sides")


class BlueShape:
    def generate_shape(self, nr_sides, shape_str):
        print(f"Generating a blue {shape_str} with {nr_sides} sides")


class Shape:

    def __init__(self, nr_sides, shape_str, color_group):
        self.nr_sides = nr_sides
        self.shape_str = shape_str

        self.color_group = color_group

    def generate(self):
        self.color_group.generate_shape(self.nr_sides, self.shape_str)


def main():
    triangle1 = Shape(3, "triangle", RedShape())
    triangle1.generate()

    square1 = Shape(4, "square", BlueShape())
    square1.generate()

    circle1 = Shape(0, "circle", BlueShape())
    circle1.generate()


if __name__ == "__main__":
    main()
