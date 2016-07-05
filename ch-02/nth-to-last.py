from utils_lists import generateLinkedList, printLinkedList, nthToLast

def main():
    linkedList = generateLinkedList()
    printLinkedList(linkedList)
    newLinkedList = nthToLast(linkedList, 4)
    print 'camara'
    printLinkedList(newLinkedList)

if __name__ == '__main__':
    main()
