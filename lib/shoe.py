#!/usr/bin/env python3

#!/usr/bin/env python3

#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Adidas", size=9):
        self.brand = brand
        self.size = size
        self.condition = "Old"  # Initialize condition as "Old"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    # Add the cobble method
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"