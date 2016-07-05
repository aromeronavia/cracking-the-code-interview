from node import Node
from utils_lists import generateLinkedList, printLinkedList, invertLinkedList

def main():
    linkedList = generateLinkedList()
    print 'Normal linked list'
    printLinkedList(linkedList)
    invertedList = invertLinkedList(linkedList)
    print 'Inverted linked list'
    printLinkedList(invertedList)
    print invertedList.nextNode

if __name__ == '__main__':
    main()
