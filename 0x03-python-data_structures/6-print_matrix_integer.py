def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for i in row:
            if i  == row[len(row) - 1]:
                print('{:d}'.format(i))
                continue
            print('{:d}'.formart(i), end=" ")
    if len(row) == 0:
        print()
