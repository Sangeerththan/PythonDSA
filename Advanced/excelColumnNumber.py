letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
userInput = input("Enter column name:")


def getExcelColumNumber(column_name):
    n = len(column_name)
    column_number = 0
    try:
        for i in range(n):
            power = n - 1 - i
            index = letters.index(column_name[i]) + 1
            column_number += index * (26 ** power)
        if column_number == 0:
            raise Exception('column Not found')
        return column_number
    except ValueError:
        print("Enter valid column name")
        return 0


print(getExcelColumNumber(userInput))
