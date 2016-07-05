def main():
    a = 'aabbcc'
    b = 'ccbbaa'
    print areAnagrams(a, b)

def areAnagrams(a, b):
    a = sorted(a)
    b = sorted(b)
    return a == b

if __name__ == '__main__':
    main()
