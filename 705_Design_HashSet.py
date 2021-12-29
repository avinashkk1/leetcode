class MyHashSet:

    def __init__(self):
        self.keyRange = 7
        self.bucketList = [Bucket() for i in range(self.keyRange)]
    
    def _getHash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        keyHash = self._getHash(key)
        self.bucketList[keyHash].add(key)

    def remove(self, key: int) -> None:
        keyHash = self._getHash(key)
        self.bucketList[keyHash].remove(key)

    def contains(self, key: int) -> bool:
        keyHash = self._getHash(key)
        return self.bucketList[keyHash].contains(key)

    def print(self):  
        for i in range(self.keyRange):
            print('[', end = '')   
            self.bucketList[i].print()
            print(']')
        
       

class Bucket:
    def __init__(self) -> None:
        self.binarySearchTree = BSTree()
    
    def add(self, key):
        self.binarySearchTree.root = self.binarySearchTree.add(self.binarySearchTree.root, key)
    
    def print(self):        
        # self.binarySearchTree.printInOrder(self.binarySearchTree.root)
        self.binarySearchTree.printPreOrder(self.binarySearchTree.root)
    
    def contains(self, key):
        return self.binarySearchTree.contains(key)
    
    def remove(self, key):
        self.binarySearchTree.root = self.binarySearchTree.remove(self.binarySearchTree.root, key)
        

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right

class BSTree:
    def __init__(self):
        self.root = None 
        
    
    def add(self, root, key):
        if not root:
            root = TreeNode(key)
            return root
        
        if root.val < key:
            root.right = self.add(root.right, key)
        elif root.val > key:
            root.left = self.add(root.left, key)
        
        return root
        

    def contains(self, key):
        node = self.root
        while node:
            if node.val == key:
                return True
            if node.val < key:
                node = node.right
            else:
                node = node.left
        
        return False
    
    def _getPredecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        
        return root.val
    
    def _getSuccessor(self, root):
        root = root.right
        while root.left:
            root = root.left
        
        return root.val
    
    def remove(self, root, key):
        if not root:
            return None 
        
        if root.val < key:
            root.right = self.remove(root.right, key)
        elif root.val > key:
            root.left = self.remove(root.left, key)
        else:
            if not (root.left or root.right):
                root = None 
            elif root.right:
                root.val = self._getSuccessor(root)
                root.right = self.remove(root.right, root.val)
            else:
                root.val = self._getPredecessor(root)
                root.left = self.remove(root.left, root.val)
        
        return root
        

    def printInOrder(self, root):
        if not root:
            return
        
        self.printInOrder(root.left)
        print(root.val, end = ' ')
        self.printInOrder(root.right)
    
    def printPreOrder(self, root):
        if not root:
            return
        
        print(root.val, end = ' ')
        self.printPreOrder(root.left)
        self.printPreOrder(root.right)
        

"""
def main():
    myHashSet = MyHashSet()
    myHashSet.print()
    myHashSet.add(2)
    myHashSet.print()
    myHashSet.add(3)
    myHashSet.print()
    print(myHashSet.contains(2))
    print(myHashSet.contains(4))
    myHashSet.add(9)
    myHashSet.add(23)
    myHashSet.add(16)   
    myHashSet.add(30) 
    myHashSet.print()
    print(myHashSet.contains(23))
    myHashSet.remove(23)
    print(myHashSet.contains(23))
    myHashSet.print()
    

if __name__ == '__main__':
    main()
"""




 
       


            

