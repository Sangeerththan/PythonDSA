data = [['2 2 2', '2 2 2', '2 2 2'], ['3 3 3', '3 3 3', '3 3 3'], ['4 4 4', '4 4 4', '4 4 4'], ['5 5 5', '5 5 5', '5 5 5']]
for i in range(len(data[0])):
    print("\t".join([data[j][i] for j in range(len(data))]))