class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if not node.right:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def contains(self, data):
        return self._contains_recursive(self.root, data)
    
    def _contains_recursive(self, node, data):
        if not node:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self._contains_recursive(node.left, data)
        else:
            return self._contains_recursive(node.right, data)

    def preorder(self):
        res = []
        self._preorder_traversal(self.root, res)
        return res
    
    def _preorder_traversal(self, node, res):
        if node:
            res.append(node.data)
            self._preorder_traversal(node.left, res)
            self._preorder_traversal(node.right, res)

    def inorder(self):
        res = []
        self._inorder_traversal(self.root, res)
        return res
    
    def _inorder_traversal(self, node, res):
        if node:
            self._inorder_traversal(node.left, res)
            res.append(node.data)
            self._inorder_traversal(node.right, res)

    def postorder(self):
        res = []
        self._postorder_traversal(self.root, res)
        return res
    
    def _postorder_traversal(self, node, res):
        if node:
            self._postorder_traversal(node.left, res)
            self._postorder_traversal(node.right, res)
            res.append(node.data)

    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if not node:
            return
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)

        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                node.data = self._min_val_node(node.right).data
                node.right = self._delete_recursive(node.right, node.data)
        
        return node

    def _min_val_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def min_key(self):
        current = self.root
        while current.left:
            current = current.left
        return current.data
    
    def max_key(self):
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    def is_bst(self):
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_bst_recursive(self, node, min, max):
        if not node:
            return True
        if not (min < node.data < max):
            return False
        return (self._is_bst_recursive(node.left, min, node.data) and self._is_bst_recursive(node.right, node.data, max))

bst = BST()
arr = [15, 50, 10, 25, 40]
for i in arr:
    bst.insert(i)
print(bst.contains(30))
print(bst.preorder())
print(bst.inorder())
print(bst.postorder())
bst.delete(15)
print(bst.postorder())
print(bst.max_key())
print(bst.min_key())
print(bst.is_bst())