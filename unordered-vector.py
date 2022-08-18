import numpy as np

class UnorderedVector:
    def __init__(self, size): 
        self.size = size
        self.last_position = -1
        self.values = np.empty(self.size, dtype=int)

    #O(n)
    def print(self):
        if self.last_position == -1:
            print('empty vector')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])
    
    #O(1) - O(2)
    def insert(self, value):
        if self.last_position == self.size - 1:
            print('max size reached')
        else:
            self.last_position += 1
            self.values[self.last_position] = value

    #O(n)
    def search(self, value): 
        for i in range(self.last_position + 1):
            if value == self.values[i]:
                return i 
            
        return -1


vector = UnorderedVector(5)

vector.print()

vector.insert(2)
vector.insert(3)
vector.insert(4)
vector.insert(8)
vector.insert(9)

vector.print()

print(vector.search(2))