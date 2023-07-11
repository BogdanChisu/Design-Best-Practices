"""
-------------------------------------------------------------------------------
ADAPTER - Structural pattern
-------------------------------------------------------------------------------

https://refactoring.guru/design-patterns/adapter

Adapter is a structural design pattern that allows objects with incompatible
interfaces to collaborate.

Imagine that you're creating a stock market monitoring app. The app downloads
the stock data from multiple sources in XML format and then displays nice
looking charts and diagrams for the user.

At some point, you decide to improve the app by integrating a smart 3rd-party
analytics libray. But there's a catch: the analytics library only works with
data in JSON format.

You could change the library to work with XML. However, this might break some
existing code that relies on the library. And worse, you might not have access
to the library's source code in the first place, making this approach impossible.

SOLUTION:

You can create an adapter. This is a special object that converts the interface
of one object so that another object can understand it.

PROCESS:
    1. The adapter gets an interface, compatible with one of the existing
       objects,
    2. Using this interface, the existing object can safely call the adapter's
       methods,
    3. Upon receiving a call, the adapter passes the request to the second
       object, but in a format and order that the second object expects.
"""

class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Adaptee, Target):

    # def test(self):
    #     pass
    def request(self) -> str:
        return f"Adapted text is: {self.specific_request()[::-1]}"
        # Google: how to print a string backwards


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")



if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    adapter = Adapter()
    client_code(adapter)
    print(f"\nAdaptor: {adapter.request()}")

    # print()