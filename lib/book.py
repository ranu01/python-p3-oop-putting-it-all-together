#!/usr/bin/env python3

#!/usr/bin/env python3
class Book:
    def __init__(self, title="And Then There Were None", page_count=272):
        self.title = title
        self.page_count = page_count  # This uses the setter

    # Getter for page_count
    @property
    def page_count(self):
        return self._page_count

    # Setter for page_count
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value 
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    
        