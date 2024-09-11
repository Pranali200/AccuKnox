class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._index = 0

    def __iter__(self):
        self._index = 0 # Reset index
        return self
    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            raise StopIteration # Stop iteration when done
# taken values
rect = Rectangle(5, 10)
for dimension in rect:
    print(dimension)


#{'length': 5}
#{'width': 10}
