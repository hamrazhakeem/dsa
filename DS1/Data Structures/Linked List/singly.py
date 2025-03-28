class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        n = self.head
        while n:
            print(n.data,end='-->')
            n = n.next

    def find_length(self):
        n = self.head
        count = 0
        while n:
            count += 1
            n = n.next
        print('Length of the LL is:', count)

    def print_reverse(self):
        def recursive_print(node):
            if not node:
                return
            recursive_print(node.next)
            print(node.data, end='<--')
        recursive_print(self.head)

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def del_begin(self):
        if not self.head:
            return
        self.head = self.head.next

    def del_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def del_with_val(self, val):
        if not self.head:
            return
        if self.head.data == val:
            self.head = self.head.next
            return
        node = self.head
        while node.next:
            if node.next.data == val:
                node.next = node.next.next
                return
            node = node.next
    
    def add_after(self, data, new_data):
        if not self.head:
            return
        n = self.head
        while n:
            if n.data == data:
                new_node = Node(new_data)
                new_node.next = n.next
                n.next = new_node
                return
            n = n.next

    def add_before(self, data, new_data):
        if not self.head:
            return
        new_node = Node(new_data)
        if self.head.data == data:
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next:
            if n.next.data == data:
                new_node.next = n.next
                n.next = new_node
                return
            n = n.next

    def covert_arr_to_ll(self, arr):
        for i in arr:
            self.add_end(i)
    
    def remove_dup_in_a_sorted_ll(self):
        if not self.head or not self.head.next:
            return
        
        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def find_middle(self):
        if not self.head:
            return
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def add_middle(self, data):
        if not self.head:
            self.head = Node(data)
            return

        if not self.head.next:
            self.head.next = Node(data)
            return

        slow = fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        new_node = Node(data)
        new_node.next = slow
        prev.next = new_node

    def del_middle(self):
        if not self.head:
            return
        elif not self.head.next:
            self.head = None
            return
        
        slow = fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next

    def add_in_pos(self, pos, data):
        if pos < 0:
            return 
        
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head.next
            self.head = new_node
            return
        
        current = self.head
        for i in range(pos - 1):
            if not current:
                return
            current = current.next

        if not current:
            return
        
        new_node.next = current.next
        current.next = new_node

    def del_pos(self, pos):
        if not self.head or pos < 0:
            return
        
        if pos == 0:
            self.head = self.head.next
            return
        
        current = self.head
        for i in range(pos - 1):
            if not current.next:
                return
            current = current.next

        if not current.next:
            return
        
        current.next = current.next.next

    def search_val(self, data):
        if not self.head:
            return
        n = self.head
        while n:
            if n.data == data:
                return n
            n = n.next
        return

arr = [100, 100, 200, 200, 300, 500, 600]
ll = LinkedList()
ll.add_begin(10)
ll.add_end(20)
ll.del_with_val(1)
ll.add_after(20, 100)
ll.add_before(100, 50)
ll.covert_arr_to_ll(arr)
ll.remove_dup_in_a_sorted_ll()
print(ll.search_val(200))
print(ll.find_middle())
ll.del_middle()
ll.print()
print()
ll.print_reverse()
print()
ll.find_length()