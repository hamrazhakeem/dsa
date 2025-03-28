class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.size = 10
        self.arr = [None] * self.size

    def get_hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        if not self.arr[hash]:
            self.arr[hash] = Node(key, value)
            return
        
        current = self.arr[hash]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                current.next = Node(key, value)
                return
            current = current.next

    def __getitem__(self, key):
        hash = self.get_hash(key)
        current = self.arr[hash]
        while current:
            if current.key == key:
                return current.value
            current = current.next

    def __delitem__(self, key):
        hash = self.get_hash(key)
        if not self.arr[hash]:
            return
        current = self.arr[hash]
        if current.key == key:
            self.arr[hash] = current.next
            return
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

    def items(self):
        all_items = []
        for bucket in self.arr:
            current = bucket
            while current:
                all_items.append((current.key, current.value))
                current = current.next
        return all_items

    def __repr__(self):
        return str(self.items())

ht = HashTable()
ht['apple'] = 10
ht['banana'] = 20
del ht['apple']
print(ht)














