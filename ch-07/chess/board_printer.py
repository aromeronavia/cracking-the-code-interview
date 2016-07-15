def printBoard(board):
    for i in range(8):
        print '{0}'.format(chr(104 - i)),
        for j in range(8):
            print board[7 - i][7 - j],
        print

    print ' ',
    for i in range(8):
        print '{0}'.format(i),
