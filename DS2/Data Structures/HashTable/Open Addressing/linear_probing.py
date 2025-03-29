class HashTable:
    def __init__(self):
        self.size = 10
        self.arr = [None] * self.size

    def get_hash(self, key):
        return sum(ord(char) for char in str(key)) % self.size
    
    def __setitem__(self, key, value):
        hash = self.get_hash(key)

        start_hash = hash
        while self.arr[hash] is not None and self.arr[hash][0] != key:
            hash = (hash + 1) % self.size
            if hash == start_hash:
                raise Exception("Hash Table is full")
            
        self.arr[hash] = (key, value)

    def __getitem__(self, key):
        hash = self.get_hash(key)

        start_hash = hash
        while self.arr[hash] is not None:
            if self.arr[hash][0] == key:
                return self.arr[hash][1]
            hash = (hash + 1) % self.size
            if hash == start_hash:
                break

    def __delitem__(self, key):
        hash = self.get_hash(key)

        start_hash = hash
        while self.arr[hash] is not None:
            if self.arr[hash][0] == key:
                self.arr[hash] = None
                return
            hash = (hash + 1) % self.size
            if start_hash == hash:
                break
    
    def items(self):
        return [(item[0], item[1]) for item in self.arr if item]

    def __repr__(self):
        return str(self.items())
    
ht = HashTable()
ht['apple'] = 10
ht['banana'] = 20
print(ht['apple'])
del ht['apple']
print(ht)