from node import Node
from random import randrange

def generateLinkedList(n=5):
    firstNode = generateRandomNode()
    aux = firstNode
    for i in range(n):
        aux.nextNode = generateRandomNode()
        aux = aux.nextNode

    return firstNode

def generateRandomNode():
    return Node(randrange(0, 5))

def printLinkedList(node):
    while node:
        print node
        node = node.nextNode

"""
2. 0 For the lulz, invert a linked list
"""
def invertLinkedList(initialNode):
    lastNode = getLastNode(initialNode)
    _invertLinkedList(initialNode)
    initialNode.nextNode = None
    return lastNode

def _invertLinkedList(initial):
    nextNode = initial.nextNode
    if nextNode and nextNode.nextNode:
        _invertLinkedList(nextNode)

    nextNode.nextNode = initial

def getLastNode(linkedList):
    while linkedList.nextNode:
        linkedList = linkedList.nextNode

    return linkedList

"""
2.1 Write code to remove duplicates from an unsorted linked list
"""
def deleteDuplicates(linkedList):
    elements = {}
    previous = linkedList
    while linkedList:
        if str(linkedList.value) in elements:
            previous.nextNode = linkedList.nextNode
        else:
            elements[str(linkedList.value)] = 1
            previous = linkedList

        linkedList = linkedList.nextNode

    print elements

"""
2.2 Implement an algorithm to  nd the nth to last element of a singly linked list
"""
def nthToLast(linkedList, n):
    i = 0
    while i < n and linkedList:
        linkedList = linkedList.nextNode
        i += 1

    return linkedList

"""
2. 3 is impossible, due the fact that in a single linked list,
we can't have a reference to a previous element of the list from
any node. So, given a node C in a list of the form A->B->C->D->E, its
impossible to return a list without the node C: A->B->D->E if we dont have the first reference to the list
"""

def sumNumbersWithLists(listA, listB):
    if not (listA and listB):
        return 0

    result = Node()
    firstNode = result
    while listA or listB:
        a = listA.value
        b = listB.value
        carry = (a + b) / 10
        sumatory = (a + b) % 10
        result.value = result.value + sumatory
        if carry:
            result.nextNode = Node(carry)
            result = result.nextNode

        if listA.nextNode:
            listA = listA.nextNode
        else:
            listA.value = 0

        if listB.nextNode:
            listB = listB.nextNode
        else:
            listB.value = 0

        result.nextNode = Node()
        result = result.nextNode

    return firstNode
