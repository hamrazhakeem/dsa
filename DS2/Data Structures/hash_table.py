class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash]):
            if element[0] == key:
                self.arr[hash][idx] = (key, value)
                return
        self.arr[hash].append((key, value))

    def __getitem__(self, key):
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]
            
    def __delitem__(self, key):
        hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash]):
            if element[0] == key:
                del self.arr[hash][idx]
                break

ht = HashTable()
ht['march 6'] = 10
ht['march 17'] = 30
ht['banana'] = 20
del ht['banana']
print(ht['march 6'])
print(ht.arr)