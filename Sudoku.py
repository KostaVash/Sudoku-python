import random
from random import seed
from random import randint
import time
global mat
SIZE = 9

#creating a grid 9 by 9 , with value 0 in each cell#
def create_grid():
    global mat
    mat= [[0 for x in range(SIZE)] for y in range(SIZE)] 
    for i in range(SIZE):
        for j in range(SIZE):
            mat[i][j]=0
    return mat


#return True if the number doest exsit in the row#
def check_row(row,column,number):
    global mat
    for i in range(SIZE):

        if(number==mat[row][i]):      
            return False

    return True

#return True if the number doest exsit in the column#
def check_column(row,column,number):
    global mat
    for i in range(SIZE):
    
        if(number==mat[i][column]):
            return False
    return True
        

#return the section, anumber between 1-3#
def get_section(number):

    if(number >=0 and number<=2):
        return 0,3

    elif (number >=3 and number <=5):
        return 3,6

    else:
        return 6,9

#check if we have the same number in the box [(3*3) grid]#        
def check_box(row,column,number):
    global mat
    start_row,end_row = get_section(row)
    start_column,end_column = get_section(column)

    for i in range(start_row,end_row):
        for j in range(start_column,end_column):
            if(number==mat[i][j]):
                return False
    return True


#return True if we can add the number to the board or False if we cant#
def add_number(row,column,number):
    global mat
    if((number>0 and number<=9)and check_box(row,column,number)==True and check_column(row,column,number)==True and check_row(row,column,number)==True):
        return True
    return False

def create_solution():
    global mat
    for i in range(SIZE):
        for j in range(SIZE):

            if(mat[i][j]==0):
                for num in range(1,SIZE+1):
                
                    if(add_number(i,j,num)):

                        mat[i][j]=num
                        if(valid_solution()==True):
                            return mat
                        create_solution()
                        mat[i][j]=0 #backtraking
                return  #if we can't solve the puzzle#
    
    return            
         

def create_board():
    global mat
    i=random.randint(0,SIZE-1)
    j =random.randint(0,SIZE-1)
    count=1
    while(board_is_empty()==True and count <=15):
        if(mat[i][j]==0):
                num=random.randint(1,SIZE)
                if(add_number(i,j,num)):
                    mat[i][j]=num
                    count+=1
        i=random.randint(0,SIZE-1)
        j =random.randint(0,SIZE-1)
        
    return        

def valid_solution():
    global mat
    if(board_is_empty()==True):
        return False
    for i in range(SIZE):
            for j in range(SIZE):
                for num in range(1,SIZE+1):

                    if(add_number(i,j,num)==True):
                        break
                    else:
                        return False
    return True





#check if there free space in the board(0 is free)#
def board_is_empty():
    global mat
    for i in range(SIZE):
        for j in range(SIZE):
            if(mat[i][j]==0):
                return True
    return False

#priniting the matrix with the borders#
def print_mat():
    global mat
    for i in range(SIZE):
        if(i%3==0):
            print("-----------------------------------------")

        for j in range(SIZE+1):

            if(j%3==0 ):
                print("||",end =" ")

            else:
                print("|",end =" ")

            if((i>=0 and i<SIZE)and (j>=0 and j<SIZE)):
                if(mat[i][j]==0 or mat[i][j]==None):
                    print(" ",end =" ")
                else:
                    print((mat[i][j]) ,end =" ")

        print(" ")
        
    print("-----------------------------------------")
    

def remove_cells():
    global mat
    count=30
    while(count>0):
        i=random.randint(0,SIZE-1)
        j =random.randint(0,SIZE-1)
        if(mat[i][j]!=0):
            mat[i][j]=0
            count-=1
    return mat


def main():
        count_failed=0
        count_succsed=0
        count=0
        start_time = time.time()

        create_grid()
        create_board()
        print_mat()
        create_solution()
        count+=1
        ##print_mat(mat)
        ##mat=remove_cells(mat)
        ##print_mat(mat)
        ##mat= create_solution(mat)
        ##print_mat(mat)
        if(valid_solution()==False):
            print("No solution")
            count_failed+=1
        else:
            count_succsed+=1
            print("The Solution is : ")
            print_mat(mat)
        print("--- %s seconds ---" % (time.time() - start_time))
        print("failed ",count_failed,"succsed",count_succsed,"count",count)

main()
