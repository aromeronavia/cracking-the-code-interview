from random import randrange
from node import Node
from utils_lists import generateLinkedList, printLinkedList, deleteDuplicates

def main():
    linkedList = generateLinkedList()
    printLinkedList(linkedList)
    deleteDuplicates(linkedList)
    print 'camara'
    printLinkedList(linkedList)

if __name__ == '__main__':
    main()
