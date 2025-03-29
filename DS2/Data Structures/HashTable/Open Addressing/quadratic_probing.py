class HashTable:
    def __init__(self):
        self.size = 10
        self.arr = [None] * self.size

    def get_hash(self, key):
        return sum(ord(char) for char in str(key)) % self.size
    
    def quadratic_probe(self, method, original_hash, key, value=None):
        if method == 'set_method':
            i = 1
            while i <= self.size:
                probe_hash = (original_hash + i**2) % self.size

                if not self.arr[probe_hash] or self.arr[probe_hash][0] == key:
                    self.arr[probe_hash] = (key, value)
                    return
                
                i += 1
        elif method == 'get_method':
            i = 1
            while i <= self.size:
                probe_hash = (original_hash + i**2) % self.size

                if self.arr[probe_hash]:
                    if self.arr[probe_hash][0] == key:
                        return self.arr[probe_hash][1]
                
                i += 1
        else:
            i = 1
            while i <= self.size:
                probe_hash = (original_hash + i**2) % self.size

                if self.arr[probe_hash]:
                    if self.arr[probe_hash][0] == key:
                        self.arr[probe_hash] = None
                        return

                i += 1

    def __setitem__(self, key, value):
        hash = self.get_hash(key)

        if not self.arr[hash] or self.arr[hash][0] == key:
            self.arr[hash] = (key, value)
            return
        
        self.quadratic_probe('set_method', hash, key, value)

    def __getitem__(self, key):
        hash = self.get_hash(key)
        
        if self.arr[hash]:
            if self.arr[hash][0] == key:
                return self.arr[hash][1]
        
        self.quadratic_probe('get_method', hash, key)

    def __delitem__(self, key):
        hash = self.get_hash(key)

        if self.arr[hash]:
            if self.arr[hash][0] == key:
                self.arr[hash] = None
                return
            
        self.quadratic_probe('delete_method', hash, key)

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