class HashTable:
    def __init__(self):
        self.size = 11
        self.arr = [None] * self.size

    def get_hash(self, key):
        return sum(ord(char) for char in str(key)) % self.size
    
    def get_hash_2(self, key):
        prime = 7
        return prime - (sum(ord(char) for char in str(key))) % prime
    
    def __setitem__(self, key, value):
        hash = self.get_hash(key)

        if not self.arr[hash] or self.arr[hash][0] == key:
            self.arr[hash] = (key, value)
            return
        
        hash2 = self.get_hash_2(key)
        i = 1

        while i <= self.size:
            new_hash = (hash + i * hash2) % self.size

            if not self.arr[new_hash] or self.arr[new_hash][0] == key:
                self.arr[new_hash] = (key, value)
                return
            
            i += 1
            
    def __getitem__(self, key):
        hash = self.get_hash(key)
        
        if self.arr[hash]:
            if self.arr[hash][0] == key:
                return self.arr[hash][1]
        
        hash2 = self.get_hash_2(key)

        i = 1
        while i <= self.size:
            new_hash = (hash + i * hash2) % self.size

            if self.arr[new_hash]:
                if self.arr[new_hash][0] == key:
                    return self.arr[new_hash][1]
                
            i += 1
            
    def __delitem__(self, key):
        hash = self.get_hash(key)

        if self.arr[hash]:
            if self.arr[hash][0] == key:
                self.arr[hash] = None
                return
        
        hash2 = self.get_hash_2(key)
        
        i = 1
        while i <= self.size:
            new_hash = (hash + i * hash2) % self.size

            if self.arr[new_hash]:
                if self.arr[new_hash][0] == key:
                    self.arr[new_hash] = None
                    return
                
            i += 1

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