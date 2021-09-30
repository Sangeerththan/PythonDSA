# Reading number of rows
row = int(input('Enter how many lines? '))


def firsthalf(rows):
    for i in range(1, rows + 1):

        # for space
        for j in range(1, rows + 1 - i):
            print(' ', end='')

        # for increasing pattern
        for j in range(1, i + 1):
            print(j, end='')

        # for decreasing pattern
        for j in range(i - 1, 0, -1):
            print(j, end='')

        # Moving to next line
        print()


def bottomHalf(rows):
    for i in range(rows, 0, -1):

        # for space
        for j in range(1, rows + 2 - i):
            print(' ', end='')

        # for increasing pattern
        for j in range(1, i + 1):
            print(j, end='')

        # for decreasing pattern
        for j in range(i - 1, 0, -1):
            print(j, end='')
            # Moving to next line


def pattern(rows):
    firsthalf((rows // 2) + 1)
    bottomHalf(rows // 2)


pattern(row)
