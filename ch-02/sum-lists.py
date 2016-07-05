from utils_lists import generateLinkedList, printLinkedList, sumNumbersWithLists

def main():
    listA = generateLinkedList(3)
    listB = generateLinkedList(3)
    print 'list A'
    printLinkedList(listA)
    print 'list B'
    printLinkedList(listB)
    result = sumNumbersWithLists(listA, listB)
    print 'result'
    printLinkedList(result)

if __name__ == '__main__':
    main()
