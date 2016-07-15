from tree import TreeNode
from random import randrange

def main():
    node = TreeNode(4)
    for i in range(5):
        insert(node, TreeNode(randrange(0, 10)))
    print 'inOrder'
    inOrder(node)
    print 'preOrder'
    preOrder(node)
    print 'postOrder'
    postOrder(node)
    print 'inserting 8 in tree'
    insert(node, TreeNode(1))
    inOrder(node);

def inOrder(node):
    if not node:
        return
    inOrder(node.left)
    print node
    inOrder(node.right)

def preOrder(node):
    if not node:
        return
    print node
    preOrder(node.left)
    preOrder(node.right)

def postOrder(node):
    if not node:
        return
    postOrder(node.left)
    postOrder(node.right)
    print node

def insert(node, newNode):
    if newNode.value > node.value:
        if not node.right:
            node.right = newNode
        else:
            insert(node.right, newNode)
    else:
        if not node.left:
            node.left = newNode
        else:
            insert(node.left, newNode)

if __name__ == '__main__':
    main()
