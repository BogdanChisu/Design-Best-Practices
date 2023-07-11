"""
-------------------------------------------------------------------------------
COMPOSITE - Structural pattern
-------------------------------------------------------------------------------

Composite is a structural design pattern that lets you compose objects into tree
structures and then work with these structures as if they were individual
objects.

Here we attempt to make an organizational hierarchy with sub-organization,
 which may have subsequent sub-organizations, such as:
GeneralManager                                   [Composite]
      Manager1                                   [Composite]
              Developer11                        [Leaf]
              Developer12                        [Leaf]
      Manager2                                   [Composite]
              Developer21                        [Leaf]
              Developer22                        [Leaf]
"""


class LeafElement:
    """class representing objects at the bottom or Leaf of hierarchy tree"""

    def __init__(self, *args):
        '''Takes the first positional argument and assigns to member variable
        "position"'''
        self.position = args[0]

    def show_details(self):
        print("\t", end = "")
        print(self.position)


class CompositeElement:
    '''Class representing objects at any level of the hierarchy tree
    except for the bottom or leaf level. Maintains the child objects by
    adding and removing them from the tree structure.'''

    def __init__(self, *args):
        '''Takes the first positional argument and assigns to member variable
        "position". Initializes a list of children elements.'''
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        '''Removes the supplied child element from the list of children
        elements "children"'''
        self.children.remove(child)

    def show_details(self):
        '''Prints the details of the component element first. Then, iterates
        over each of its children, prints their details by calling their
        show_details method'''
        print(self.position)
        for child in self.children:
            print("\t", end = "")
            child.show_details()

def main():
    topLevelMenu = CompositeElement("General Manager")
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")

    subMenuItem11 = LeafElement("Developer11")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer12")

    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem21)
    subMenuItem2.add(subMenuItem22)

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.show_details()

if __name__ == "__main__":
    main()
