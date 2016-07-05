def main():
    string = 'abcdefg'
    if hasOnlyUniqueCharacters(string):
        print 'hellyeah'

    string = 'aabcd'
    if not hasOnlyUniqueCharacters(string):
        print 'ni pedo'

def hasOnlyUniqueCharacters(string):
    adyacentList = [False for i in range(128)]
    for char in string:
        if adyacentList[ord(char)]:
           return False
        adyacentList[ord(char)] = True

    return True

if __name__ == '__main__':
    main()
