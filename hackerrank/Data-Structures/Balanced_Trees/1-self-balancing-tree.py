#!/usr/bin/python3

# An AVL tree


class Node(object):
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree(object):
    def leftRotate(self, Z):
        Y = Z.right
        T2 = Y.left

        # perform rotation
        Y.left = Z
        Z.right = T2

        # update heights
        Y.height = 1 + max(self.getHeight(Y.left),
                           self.getHeight(Y.right))
        Z.height = 1 + max(self.getHeight(Z.left),
                           self.getHeight(Z.right))
        return Y

    def rightRotate(self, Z):
        Y = Z.left
        T3 = Y.right

        # perform rotation
        Y.right = Z
        Z.left = T3

        # update heights
        Y.height = 1 + max(self.getHeight(Y.left),
                           self.getHeight(Y.right))
        Z.height = 1 + max(self.getHeight(Z.left),
                           self.getHeight(Z.right))
        return Y

    def getHeight(self, root):
        if root is None:
            return 0

        return root.height

    def getBalance(self, root):
        if root is None:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        if root is None:
            return

        print(root.info, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.info:
            root.left = self.insert(root.left, key)
        elif key > root.info:
            root.right = self.insert(root.right, key)

        # update height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # check balance factor
        balance = self.getBalance(root)

        # L-L case
        if balance > 1 and key < root.left.info:
            return self.rightRotate(root)

        # R-R case
        if balance < -1 and key > root.right.info:
            return self.leftRotate(root)

        # L-R case
        if balance > 1 and key > root.left.info:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.info:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


if __name__ == '__main__':
    myTree = AVL_Tree()
    root = None

    # import pdb; pdb.set_trace()
    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)

    # Preorder Traversal
    print("Preorder traversal of the",
          "constructed AVL tree is")
    myTree.preOrder(root)
    print()
