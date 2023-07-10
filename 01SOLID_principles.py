###################################
# SOLID
###################################
"""
SOLID is a set of five object-oriented design principles that can help you write
more maintainable, flexible and scalable code based on well-designed, cleanly 
structured classes.

1. | Single Responsibility
-------------------------------------------------------------------------------

     Make things (classes, functions, etc.) responsible for fullfilling one type
     of role. 

2. | Opened/Closed
-------------------------------------------------------------------------------

     Be able to add new functionality to existing code easily without modifying
     existing code.
     
     e.g. Use abstract classes. These can define what the subclasses will
     require and strengthen Principle 1 by separating code duties. 
     
3. | Liskov Substitution
-------------------------------------------------------------------------------

     When a class inherits from another class, the program shouldn't need to
     hack anything to use the subclass.
     
     e.g. Define constructor arguments to keep inheritance flexible.

4. | Interface Segregation
-------------------------------------------------------------------------------

     Make interfaces (parent abstract classes) more specific, rather than
     generic.
     
     e.g. Create more interfaces (classes) if needed and/or provide objects to
     constructors 

5. | Dependency Inversion
-------------------------------------------------------------------------------

     Make classes depend on abstract classes rather than non-abstract classes.
     
     e.g. Make classes inherit from abstract classes
"""