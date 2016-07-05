def main():
    string = "aaaabbbbccccdd"
    compressedString = compressString(string)
    print compressedString

def compressString(string):
    char = string[0]
    accumulator = 1
    compressedString = []
    for i in range(1, len(string), 1):
        if string[i] == char:
            accumulator += 1
        else:
            compressedString.append(str(accumulator))
            compressedString.append(char)
            char = string[i]
            accumulator = 1

    compressedString.append(str(accumulator))
    compressedString.append(char)

    return "".join(compressedString)

main()
