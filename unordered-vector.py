import numpy as np

class UnorderedVector:
    def __init__(self, size): 
        self.size = size
        self.last_position = -1
        self.values = np.empty(self.size, dtype=int)

    #O(N)
    def print(self):
        if self.last_position == -1:
            print('empty vector')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])

    def insert(self, v):
        if self.last_position == self.size - 1:
            print('max size reached')
        else:
            self.last_position += 1
            self.values[self.last_position] = v


vector = UnorderedVector(5)

vector.print()

vector.insert(2)
vector.insert(3)
vector.insert(4)
vector.insert(8)
vector.insert(9)

vector.print()
