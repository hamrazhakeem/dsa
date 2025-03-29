class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        return sum(ord(char) for char in str(key)) % self.MAX
    
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

    def items(self):
        all_items = []
        for index in self.arr:
            for entry in index:
                all_items.append(entry)
        return all_items

    def __repr__(self):
        return str(self.items())

ht = HashTable()
ht['apple'] = 10
ht['banana'] = 20
print(ht['apple'])
del ht['apple']
print(ht)