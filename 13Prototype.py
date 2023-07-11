"""
PROTOTYPE - Creational Pattern

https://python.en.sdacademy.pro/coursebook/design_patterns_and_good_practices/creational_patterns/prototype/

Prototype is a design pattern that allows you to create objects in a process
that is divided into two stages:
- creating a base object(e.g. partially completed) which is a copy of the
  finished object
- setting the rest of the object's field

This pattern can be used when we are working on a large application whose
performance is a key factor and creating a prototype can improve the operation
of our application.

PYTHON COPY
-------------------------------------------------------------------------------

An assignment in Python does not copy an object, it only creates another
reference to it. Copy modules can be used for copying:
- shallow copy: copy.copy(x)
- deep copy: copy.deepcopy(x)

The difference between the two methods is when you copy complex objects, i.e.
objects that contain other objects such as lists or class instances:
- shallow copy constructs a new composite object and places references to
  objects from the original composite object
- deep copy constructs a new compound object and recursively places copies of
  objects from the original compound object into it

EXAMPLE
-------------------------------------------------------------------------------

The following example shows a simple prototype implementation that uses a copy
module and a shallow copy. In this case it is sufficient because the
PythonCodeFile class does not contain complex objects.
"""

import copy

class PythonCodeFile:
    def __init__(self, license_content, file_extension, code = '',
                 file_name = ''):
        self._license_content = license_content
        self._code = code
        self._file_name = file_name
        self._file_extension = file_extension

    @property
    def license_content(self):
        return self._license_content

    @license_content.setter
    def license_content(self, value):
        self._license_content = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def file_extension(self):
        return self._file_extension

    @file_extension.setter
    def file_extension(self, value):
        self._file_extension = value

    def create_clone(self):
        return copy.copy(self)

    def __str__(self):
        return f"File: {self._file_name}.{self._file_extension}, " \
               f"license = [{self._license_content}]," \
               f"code = [{self._code}]"


class PythonCodeFileManager:
    _base_file = PythonCodeFile('SDA', 'py')

    @staticmethod
    def create_file_with_content(file_name, code):
        base_file_clone = PythonCodeFileManager._base_file.create_clone()
        base_file_clone.file_name = file_name
        base_file_clone.code = code
        return base_file_clone

def main():
    file_1 = PythonCodeFileManager.create_file_with_content('zen_of_python',
                                                            'import this')
    file_2 = PythonCodeFileManager.create_file_with_content('test_file', 'test')
    print(file_1)
    print(file_2)

if __name__ == '__main__':
    main()