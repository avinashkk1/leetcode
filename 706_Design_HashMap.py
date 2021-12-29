class TreeNode:
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
        
class BSTree:
    def __init__(self):
        self.root = None
    
    def insertOrUpdate(self, root, key, value):
        if not root:
            root = TreeNode(key, value)
        elif root.key < key:
            root.right = self.insertOrUpdate(root.right, key, value)
        elif root.key > key:
            root.left = self.insertOrUpdate(root.left, key, value)
        else:
            root.value = value
        
        return root

    def get(self, key):
        node = self.root
        while node:
            if node.key == key:
                return node.value
            if node.key < key:
                node = node.right
            else:
                node = node.left
        
        return -1
    
    def _getSuccessor(self, root):
        root = root.right
        while root.left:
            root = root.left
        
        return (root.key, root.value)

    
    def _getPredecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        
        return (root.key, root.value)
    
    
    def remove(self, root, key):
        if not root:
            return None
        
        if root.key < key:
            root.right = self.remove(root.right, key)
        elif root.key > key:
            root.left = self.remove(root.left, key)
        else:
            if not (root.left or root.right):
                return None
            if root.right:
                (root.key, root.value) = self._getSuccessor(root)
                root.right = self.remove(root.right, root.key)
            else:
                (root.key, root.value) = self._getPredecessor(root)
                root.left = self.remove(root.left, root.key)
        
        return root
                
        
        
class Bucket:
    def __init__(self):
        self.tree = BSTree()
    
    def insertOrUpdate(self, key, value):
        self.tree.root = self.tree.insertOrUpdate(self.tree.root, key, value)
    
    def get(self, key):
        return self.tree.get(key)
    
    def remove(self, key):
        self.tree.root = self.tree.remove(self.tree.root, key)
            

class MyHashMap:

    def __init__(self):
        self.keyRange = 769
        self.bucketList = [Bucket() for i in range(self.keyRange)]
    
    def _getHash(self, key):
        return key % self.keyRange

    def put(self, key: int, value: int) -> None:
        keyHash = self._getHash(key)
        self.bucketList[keyHash].insertOrUpdate(key, value)
                
    def get(self, key: int) -> int:
        keyHash = self._getHash(key)
        return self.bucketList[keyHash].get(key)

    def remove(self, key: int) -> None:
        keyHash = self._getHash(key)
        self.bucketList[keyHash].remove(key)
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)