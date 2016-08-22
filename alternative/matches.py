def match(a, b):
    if len(a) != len(b):
        return False

    return _match(a, b, 0, len(a))


def _match(a, b, i, length):
    if i == length:
        return True
    return a[i] == b[i] and _match(a, b, i + 1, length)


if __name__ == '__main__':
    a = 'aadasd'
    b = 'aad2sa'
    print match(a, a)
