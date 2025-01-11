class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        n = self.head
        while n:
            print(n.data, end='-->')
            n = n.next

    def print_reverse(self):
        n = self.tail
        while n:
            print(n.data, end='<-->')
            n = n.prev

    def add_begin(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def convert_arr_to_ll(self, arr):
        for i in arr:
            self.add_end(i)

    def del_with_val(self, data):
        if not self.head:
            return

        if self.head.data == data:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return        

        n = self.head
        while n:
            if n.data == data:
                if n == self.tail:
                    self.tail = n.prev
                    self.tail.next = None
                else:
                    n.prev.next = n.next
                    n.next.prev = n.prev
            n = n.next

    def add_after(self, val, data):
        if not self.head:
            return
        
        new_node = Node(data)

        n = self.head
        while n:
            if n.data == val:
                new_node.next = n.next
                new_node.prev = n

                if n.next:
                    n.next.prev = new_node
                else:
                    self.tail = new_node
                return
            
            n = n.next

    def add_before(self, val, data):
        if not self.head:
            return
        
        new_node = Node(data)

        n = self.head
        while n:
            if n.data == val:
                new_node.next = n
                if n == self.head:
                    self.head.prev = new_node
                    self.head = new_node
                else:
                    new_node.prev = n.prev
                    n.prev.next = new_node
                    n.prev = new_node
                return
            n = n.next

    def remove_duplicates_in_a_sorted_doubly_linked_list(self):
        if not self.head or not self.head.next:
            return
        
        current = self.head
        while current.next:
            if current.data == current.next.data:
                dup = current.next
                current.next = dup.next
                if dup.next:
                    dup.next.prev = current
                else:
                    self.tail = current
            else:
                current = current.next