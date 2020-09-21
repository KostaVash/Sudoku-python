import random

SIZE = 9

#creating a grid 9 by 9 , with value 0 in each cell#


def create_grid():
    """creating empty matrix

    Returns:
        a matrix 9*9 with 0 in each cell
    """
    matt = [[0 for row_i in range(SIZE)] for column_j in range(SIZE)]
    for row_i in range(SIZE):
        for column_j in range(SIZE):
            matt[row_i][column_j] = 0
    return matt


def get_section(number):
    """return the section, a number between 0-9

    Args:
        number (int): number between 0-8

    Returns:
        [int]: number between 0-9
    """
    if(number >= 0 and number <= 2):
        return 0, 3

    elif (number >= 3 and number <= 5):
        return 3, 6

    else:
        return 6, 9

#check if we have the same number in the box [(3*3) grid]#


def fill_box(mat, row, column):
    """[fill 3*3 box in the matrix with a random number between 1-9]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9 ]
        row ([int]): [number between 0-8]
        column ([int]): [number between 0-8]
    """
    start_row, end_row = get_section(row)
    start_column, end_column = get_section(column)
    numbers=[1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)
    count = 0
    for row_i in range(start_row, end_row):
        for column_j in range(start_column, end_column):
            mat[row_i][column_j] = numbers[count]
            count += 1


def fill_all_boxes(mat):
    """[fill all the boxes in the matrix]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
    """
    for row in range(0, SIZE, 3):
        for column in range(0, SIZE, 3):
            fill_box(mat, row, column)


def sorting_row(mat, row, column, sorted_mat):
    """[sort the row in the matrix,
    sorted row is when we have every number between 1-9 only 1 time ]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
        row ([int]): [number of the row]
        column ([int]): [number of the column]
        sorted_mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
    """
    # array that saved if the numbers appered in the row than it will changed in the array to 1 in the position of the number #
    checked = [0]*9
    for column_j in range(0, SIZE):
        num = mat[row][column_j]
        # if the number doesnt registered , so we register him #
        if(checked[num-1] == 0):
            checked[num-1] = 1
            sorted_mat[row][column_j] = 1
        # if the number registerd we searching for unregisterd number in his box (3*3) for unregisterd number#
        else:
            if(sorted_mat[row][column_j] == 0):
                new_num, new_row, new_column = find_num_in_cell_to_row(
                    mat, row, column_j, checked, num, sorted_mat, 0)
            else:
                new_num, new_row, new_column = find_num_in_cell_to_row(
                    mat, row, column_j, checked, num, sorted_mat, 1)
             # if we didnt found unregisterd number we go for the first instance of the duplicated number#
            if(new_num == 0):
                sorted_mat[row][column_j] = 1
                #go back to the first duplicated number and try to swap him #
                for column_j in range(0, SIZE):

                    # searching for the first instance of the duplicated numbers#
                    if(mat[row][column_j] == num):

                        #searching for unregisterd number to swap them #
                        if(column_j <= column):
                            new_num, new_row, new_column = find_num_in_cell_to_row(
                                mat, row, column_j, checked, num, sorted_mat, 1)
                        else:
                            new_num, new_row, new_column = find_num_in_cell_to_row(
                                mat, row, column_j, checked, num, sorted_mat, 0)

                        if(new_num != 0):
                            #sorted_mat[new_row][new_column]=2+row#
                            swap_numbers(mat, row, column_j,
                                         new_row, new_column)
                            checked[new_num-1] = 1
                            sorted_mat[row][column_j] = 1
                        else:
                            if(row % 3 != 2):
                                PAS_row(mat, row, column_j,
                                        checked, num, sorted_mat)
                        break

            else:
                #sorted_mat[new_row][new_column]=2+row#
                swap_numbers(mat, row, column_j, new_row, new_column)
                checked[new_num-1] = 1
                sorted_mat[row][column_j] = 1


def sorting_column(mat, row, column, sorted_mat):
    """[sort the column in the matrix,
    sorted column is when we have every number between 1-9 only 1 time ]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
        row ([int]): [number of the row]
        column ([int]): [number of the column]
        sorted_mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
    """
    # array that saved if the numbers appered in the row than it will changed in the array to 1 in the position of the number #
    checked = [0]*9
    for row_i in range(0, SIZE):
        num = mat[row_i][column]
        # register the number #
        if(checked[num-1] == 0):
            checked[num-1] = 1
            if sorted_mat[row_i][column] == 0:
                sorted_mat[row_i][column] = 1
        # if the number already registerd search for unregisterd number#
        else:
            if(sorted_mat[row_i][column] == 0):
                new_num, new_row, new_column = find_num_in_cell_to_column(
                    mat, row_i, column, checked, num, sorted_mat, 0)
            else:
                new_num, new_row, new_column = find_num_in_cell_to_column(
                    mat, row_i, column, checked, num, sorted_mat, 1)

            if(new_num == 0):
                sorted_mat[row_i][column] = 1
                #go back to the first duplicated number and try to swap him #
                # searching for the duplicated ins
                for row_i in range(0, SIZE):

                    if(mat[row_i][column] == num):
                        if(row_i <= row):
                            new_num, new_row, new_column = find_num_in_cell_to_column(
                                mat, row_i, column, checked, num, sorted_mat, 1)
                        else:
                            new_num, new_row, new_column = find_num_in_cell_to_column(
                                mat, row_i, column, checked, num, sorted_mat, 0)

                        if(new_num != 0):
                            #sorted_mat[new_row][new_column]=2+column#
                            swap_numbers(mat, row_i, column,
                                         new_row, new_column)
                            checked[new_num-1] = 1
                            sorted_mat[row_i][column] = 1
                        else:
                            if (column % 3 != 2):
                                PAS_column(mat, row_i, column,
                                           checked, num, sorted_mat)
                        break

            else:
                #sorted_mat[new_row][new_column]=2+column#
                swap_numbers(mat, row_i, column, new_row, new_column)
                checked[new_num-1] = 1
                sorted_mat[row_i][column] = 1


def find_num_in_cell_to_row(mat, row, column, checked, num, sorted_mat, state):
    """[finding number to replace the number in mat[row][column]]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
        row ([int]): [the index of the row]
        column ([int]): [the index of the column]
        checked ([array]): [array of the registerd numbers]
        num ([int]): [the number we need to replace]
        sorted_mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
        state ([int]): [if it sorted or not , 0- not sorted , 1 - sorted]

    Returns:
        [type]: [description]
    """
    starting_row, ending_row = get_section(row)
    starting_column, ending_column = get_section(column)
    if(state == 0):
        for row_i in range(starting_row, ending_row):
            for column_j in range(starting_column, ending_column):

                # searchiong for unregisterd number#
                if((sorted_mat[row_i][column_j] == 0) and row_i != row):
                    tmp_num = mat[row_i][column_j]
                    if(checked[tmp_num-1] == 0):
                        return tmp_num, row_i, column_j

    for row_i in range(row, ending_row):
        tmp_num = mat[row_i][column]
        #searching for registerd number in the column#
        if(checked[tmp_num-1] == 0 and sorted_mat[row_i][column] == 1):
            return tmp_num, row_i, column
    return 0, 0, 0


def find_num_in_cell_to_column(mat, row, column, checked, num, sorted_mat, state):
    """[finding number to replace the number in mat[row][column]]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
        row ([int]): [the index of the row]
        column ([int]): [the index of the column]
        checked ([array]): [array of the registerd numbers]
        num ([int]): [the number we need to replace]
        sorted_mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
        state ([int]): [if it sorted or not , 0- not sorted , 1 - sorted]

    Returns:
        [type]: [description]
    """

    starting_row, ending_row = get_section(row)
    starting_column, ending_column = get_section(column)
    if(state == 0):
        for column_j in range(starting_column, ending_column):
            for row_i in range(starting_row, ending_row):

                if((sorted_mat[row_i][column_j] == 0) and column != column_j):
                    tmp_num = mat[row_i][column_j]

                    if(checked[tmp_num-1] == 0):
                        return tmp_num, row_i, column_j

    # search in the row that allready sorted#
    for column_j in range(column, ending_column):
        tmp_num = mat[row][column_j]

        if(checked[tmp_num-1] == 0 and sorted_mat[row][column_j] == 1):
            return tmp_num, row, column_j
    return 0, 0, 0


def swap_numbers(mat, old_row, old_column, new_row, new_column):
    """[swapping the values from mat[old_row][old_column] and mat[new_row][new_column]]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
        old_row ([int]): [the index of the old row]
        old_column ([int]): [the index of the old column]
        new_row ([int]): [the index of the new row]
        new_column ([int]): [the index of the new column]
    """
    tmp = mat[old_row][old_column]
    mat[old_row][old_column] = mat[new_row][new_column]
    mat[new_row][new_column] = tmp


def PAS_row(mat, row, column, checked, num, sorted_mat):
    """[swaps with an adjacent cell ]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
        row ([int]): [index of the row]
        column ([int]): [index of the column]
        checked ([array]): [array of the registerd numbers]
        num ([int]): [the nubmer we need to replace]
        sorted_mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
    """
    count = 0
    last_column = 9
    while count < 18 and checked[num-1] != 0:
        for column_j in range(SIZE-1):
            if(mat[row][column_j] == num and last_column != column_j):
                swap_numbers(mat, row, column_j, row+1, column_j)

                sorted_mat[row][column_j] = 1
                num = mat[row][column_j]
                last_column = column_j
                count += 1
                break

    if checked[num-1] == 0:
        checked[num-1] = 1
        sorted_mat[row][column_j] = 1
        return


def PAS_column(mat, row, column, checked, num, sorted_mat):
    """[swaps with an adjacent cell ]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
        row ([int]): [index of the row]
        column ([int]): [index of the column]
        checked ([array]): [array of the registerd numbers]
        num ([int]): [the nubmer we need to replace]
        sorted_mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
    """
    count = 0
    last_row = 9
    while count < 18 and checked[num-1] != 0:
        for row_i in range(SIZE):
            if(mat[row_i][column] == num and last_row != row_i):
                swap_numbers(mat, row_i, column, row_i, column+1)
                sorted_mat[row_i][column] = 1
                num = mat[row_i][column]
                last_row = row_i
                count += 1
                break
    if checked[num-1] == 0:
        checked[num-1] = 1
        sorted_mat[row_i][column] = 1
        return


def check_numbers(mat, row, column):
    """[check if we have every number between 1-9 once in the column and in the row]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
        row ([int]): [the index of the row]
        column ([int]): [the index of the column]

    Returns:
        [int]: [0 - if we have duplicated numbers , 1 - if it's sorted]
    """
    checked_row = [0]*9
    checked_column = [0]*9
    for i in range(SIZE):
        if(checked_row[mat[row][i]-1] == 0):
            checked_row[mat[row][i]-1] = 1
        else:
            # print("###ERROR### - same number in row")
            return 0
        if(checked_column[mat[i][column]-1] == 0):
            checked_column[mat[i][column]-1] = 1
        else:
            # print("###ERROR### - same number in column")
            return 0
    # print("OK")
    return 1


def check_numbers_mat(mat):
    """[check for every row and column if we dont have duplicated numbers between 1-9]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]

    Returns:
         [int]: [0 - if we have duplicated numbers , 1 - if it's sorted]
    """
    count = 0

    for i in range(9):
        count = count+check_numbers(mat, i, i)
    if count == 9:
        return 1
    else:
        return 0


def print_mat(mat):
    """[print the matrix]

    Args:
        mat ([2-dimensional array]): [A 2-dimensional array of 9 by 9]
    """

    for row in range(SIZE):
        if(row % 3 == 0):
            print("-----------------------------------------")

        for column in range(SIZE+1):

            if(column % 3 == 0):
                print("||", end=" ")

            else:
                print("|", end=" ")

            if((row >= 0 and row < SIZE) and (column >= 0 and column < SIZE)):
                if(mat[row][column] == 0 or mat[row][column] == None):
                    print(" ", end=" ")
                else:
                    print((mat[row][column]), end=" ")

        print(" ")

    print("-----------------------------------------")


def main():
    mat = create_grid()
    sorted_mat = create_grid()
    fill_all_boxes(mat)

    print_mat(mat)
    print("---------#############-----------")
    for i in range(9):
        print("run number :", i)
        sorting_row(mat, i, i, sorted_mat)
        sorting_column(mat, i, i, sorted_mat)
        check_numbers(mat, i, i)
        print_mat(mat)
        print("---------#############-----------")
    print(check_numbers_mat(mat))


main()
