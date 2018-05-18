"""
Simple implementation of Binary Search Tree. No gurantee for balance.
- insert(self, val)
- delete(self, key)
- search(self, key)
- getDepth(self)
- preOrder(self)
- inOrder(self)
- postOrder(self)
- buildFromList(cls, l)

Author: Yi Zhou
Date: May 18, 2018 
"""

import random
from collections import deque




class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def get_val(self):
        return self.val
    def set_val(self, val):
        self.val = val




class BinarySearchTree:
    """
    Simple implementation of Binary Search Tree.
    """
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        """
        Set the root value
        """
        self.root = BSTNode(val)

    def insert(self, val):
        """
        Insert a value into BST.
        """
        if self.root is None:
            self.setRoot(val)
        else:
            self._insertNode(self.root, val)

    def _insertNode(self, currentNode, val):
        """
        Helper function to insert a value into BST.
        """
        if currentNode.val > val:
            if(currentNode.left):
                self._insertNode(currentNode.left, val)
            else:
                currentNode.left = BSTNode(val)
        else:
            if(currentNode.right):
                self._insertNode(currentNode.right, val)
            else:
                currentNode.right = BSTNode(val)

    def search(self, key):
        """
        Search a BSTNode satisfies BSTNode.val = key.
        if found return BSTNode, else return None.
        """
        return self._dfsSearch(self.root, key)


    def _dfsSearch(self, currentNode, key):
        """
        Helper function to search a key in BST.
        """
        if currentNode is None:
            return None
        elif currentNode.val == key:
            return currentNode
        elif currentNode.val > key:
            return self._dfsSearch(currentNode.left, key)
        else:
            return self._dfsSearch(currentNode.right, key)
    
    def delete(self, key):
        """
        Delete a key from BST
        """
        self.root = self._deleteNode(self.root, key)
    
    def _deleteNode(self, root, key):
        """
        Delete the key from the subtree rooted at root in a recursive way. Return the subtree after deletion.
        """
        if not root: 
            return None
        # Delete from the left subtree
        elif root.val > key: 
            root.left = self._deleteNode(root.left, key)
        # Delete from the right subtree
        elif root.val < key: 
            root.right = self._deleteNode(root.right, key)
        # Find it and begin to delete the node
        else:
            if root.left is None: 
                return root.right
            elif root.right is None:
                return root.left
            # root has left child and right child, replace it with the minimun value in right subtree. 
            # Then delete the minimun value in right subtree recursively. 
            else:
                temp = root.right
                while temp.left:
                    temp = temp.left
                mini = temp.val
                root.val = mini
                root.right = self._deleteNode(root.right, mini)
        return root
                    
    def getDepth(self):
        """
        Get the max depth of the BST
        """
        return self._dfsDepth(self.root, 0)

    def _dfsDepth(self, node, height):
        """
        Helper function to get the max depth of the BST
        """
        if node is None:
            return height
        else:
            return max(self._dfsDepth(node.left, height+1), self._dfsDepth(node.right, height+1))
    
    def inOrder(self):
        res = []
        def _dfs_in_order(node, res):
            if not node:
                return
            _dfs_in_order(node.left,res)
            res.append(node.val)
            _dfs_in_order(node.right,res)
        _dfs_in_order(self.root, res)
        return res
    
    def preOrder(self):
        res = []
        def _dfs_pre_order(node, res):
            if not node:
                return
            res.append(node.val)
            _dfs_pre_order(node.left,res)
            _dfs_pre_order(node.right,res)
        _dfs_pre_order(self.root, res)
        return res
    
    def postOrder(self):
        res = []
        def _dfs_post_order(node, res):
            if not node:
                return
            _dfs_post_order(node.left,res)
            _dfs_post_order(node.right,res)
            res.append(node.val)
        _dfs_post_order(self.root, res)
        return res
    
    @classmethod
    def buildFromList(cls, l):
        """
        return a BinarySearchTree object from l.
        suffle the list first for better balance.
        """
        random.seed()
        random.shuffle(l)
        BST = BinarySearchTree()
        for item in l:
            BST.insert(item)
        return BST
    
    def visulize(self):
        """
        Naive Visulization. 
        Warn: Only for simple test usage.
        """
        if self.root is None:
            print("EMPTY TREE.")
        else:
            print("-----------------Visualize Tree----------------------")
            layer = deque([self.root])
            layer_count = self.getDepth()
            while len( list(filter(lambda x:x is not None, layer) )):
                new_layer = deque([])
                val_list = []
                while len(layer):
                    node = layer.popleft()
                    if node is not None:
                        val_list.append(node.val)
                    else:
                        val_list.append(" ")
                    if node is None:
                        new_layer.append(None)
                        new_layer.append(None)
                    else:
                        new_layer.append(node.left)
                        new_layer.append(node.right)
                val_list = [" "] * layer_count + val_list
                print(*val_list, sep="  ", end="\n")
                layer = new_layer
                layer_count -= 1
            print("-----------------End Visualization-------------------")
 
def main():
    print("[BEGIN]Test Implementation of BinarySearchTree.")
    # Simple Insert Test
    BSTree = BinarySearchTree()
    BSTree.insert(0)
    BSTree.insert(1)
    BSTree.insert(2)
    BSTree.insert(-2)
    BSTree.insert(-4)
    BSTree.insert(-6)
    BSTree.insert(-1)
    BSTree.insert(-3)
    BSTree.visulize()
    # Simple Delete Test
    BSTree.delete(1)
    BSTree.visulize()
    BSTree.delete(0)
    BSTree.visulize()
    BSTree.delete(-3)
    BSTree.visulize()
    # Simple Traverse Test
    print("Traverse")
    print(BSTree.inOrder())
    print(BSTree.preOrder())
    print(BSTree.postOrder())
    # buildFromList Test
    inputList = [1,2,3,4,5]
    newBSTree = BinarySearchTree.buildFromList(inputList)
    newBSTree.visulize()
    print(newBSTree.inOrder())
    print("[END]Test Implementation of BinarySearchTree.")
    
if __name__ == "__main__":
    main()

                






