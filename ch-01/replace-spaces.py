def main():
    string = 'Que pedo banda   '
    length = 14
    print replaceSpaces(string, 14, "%20")

def replaceSpaces(string, length, replaceChar):
    string = string.rstrip()
    return string.replace(" ", replaceChar)


main()
