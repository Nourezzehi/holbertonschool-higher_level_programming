#!/usr/bin/python3
"""Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get_method"""
        return self.width

    @size.setter
    def size(self, value):
        """set_method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update"""

        if args and len(args) != 0:
            for idx in range(len(args)):
                self.id = args[idx]
                self.size = args[idx]
                self.x = args[idx]
                self.y = args[idx]
        else:
            if len(kwargs) > 0:
                key = kwargs.keys()
                for i in key:
                    if i == 'id':
                        self.id = kwargs['id']
                    elif i == 'size':
                        self.size = kwargs['size']
                    elif i == 'x':
                        self.x = kwargs['x']
                    elif i == 'y':
                        self.y = kwargs['y']
