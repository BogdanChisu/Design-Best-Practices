"""
-------------------------------------------------------------------------------
DECORATOR - Structural pattern
-------------------------------------------------------------------------------

Decorator is a structural patten that lets you attach new behaviors to objects
by placing these objects inside special wrapper objects that contain the
behaviors.

Imagine that you'e working on a notification library which lets other programs
notify their users about important events.

The initial version of the library was based on the Notifier class that had:
- a few fields
- a constructor
- a single send method

The method could accept a message argument from a client and send the message to
a list of emails that were passed to the notifier via its constructor. A third
party app which acted as a client was supposed to create and configure the
notifier object once, and then use it each time something important happened.

At some point, you realize that users of the library expect more than just
- email notifications.
- Many of them would like to receive an SMS about critical issues.
- Others would like to be notified on Facebook and, of course,
- the corporate users would love to get Slack notifications.
"""

from functools import wraps

def my_decorator(my_func):
    @wraps(my_func) # @wraps preserves function metadata like name and docstring

    def wrapper(*args, **kwargs):
        # do something before my_func is called
        print("doing something first.")

        result = my_func(*args, **kwargs)

        #do something after my_func is called
        print("Doing something after.")

        return result

    return wrapper

@my_decorator # invoke decorator
def my_func(x, y):
    """
    :param x: float value
    :param y: float value
    :return: sum of x and y
    """
    print(f"my_func is running with x = {x} and y = {y}")
    print(f"Sum is: x + y = {x+ y}")
    return x + y

def main():
    my_func(5, 3)

if __name__ == "__main__":
    main()