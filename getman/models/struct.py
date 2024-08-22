import json


class Struct:
    """
    Creates a simple data structure with named attributes from keyword arguments.

    The `Struct` class is a lightweight way to define a simple data
    structure where the attribute names and values can be passed as
    keyword arguments during initialization.

    This class allows for the creation of nested data structures as well.

    Args:
        **kwargs: Arbitrary keyword arguments where the keys represent
                the attribute names and the values represent the corresponding attribute values.
                If a value is a dictionary, it will be recursively converted into
                a `Struct` object, allowing for the creation of nested structures.

    Example:
        # Creating a simple `Struct` instance
        person = Struct(name='John', age=30, city='New York')

        # Accessing attributes
        print(person.name)  # Output: 'John'
        print(person.age)   # Output: 30
        print(person.city)  # Output: 'New York'

        # Creating a nested `Struct` instance
        address = Struct(street='123 Main St', zip_code='10001')
        person = Struct(name='John', age=30, city='New York', address=address)

        # Accessing attributes in a nested structure
        print(person.name)         # Output: 'John'
        print(person.address)      # Output: <__main__.Struct object at 0x...>
        print(person.address.street)  # Output: '123 Main St'

    Note:
        The `Struct` class does not enforce strict attribute typing,
        and attribute values can be of any type.
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, dict):
                setattr(self, key, Struct(**value))
            else:
                setattr(self, key, value)

    def __repr__(self):
        attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return f'Struct({attributes})'

    def __getattr__(self, name):
        return None

    def __str__(self):
        attributes = ', '.join(f'{key}={value}' for key, value in self.__dict__.items())
        return f'Struct: {attributes}'

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __delitem__(self, key):
        delattr(self, key)

    def to_json(self, indent=0):
        """
        Converts the `Struct` object to a JSON string.
        """

        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=indent)
