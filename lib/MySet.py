class MySet:
    def __init__(self, initial_elements=None):
        # Initialize the set with initial_elements if provided
        if initial_elements is None:
            self.dictionary = set()
        else:
            if not isinstance(initial_elements, (list, set, tuple)):
                raise TypeError("initial_elements must be a list, set, or tuple")
            self.dictionary = set(initial_elements)
    
    def add(self, element):
        # Add an element to the set
        self.dictionary.add(element)
    
    def delete(self, element):
        # Remove an element from the set
        if element in self.dictionary:
            self.dictionary.remove(element)
        else:
            raise KeyError(f"{element} not found in set")
    
    def has(self, element):
        # Check if an element is in the set
        return element in self.dictionary
    
    def size(self):
        # Return the number of elements in the set
        return len(self.dictionary)
    
    def clear(self):
        # Clear the set
        self.dictionary.clear()
    
    def __str__(self):
        # Return a string representation of the set
        return f"MySet: {{{', '.join(map(str, self.dictionary))}}}"