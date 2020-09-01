import random


SIZE = 9

#creating a grid 9 by 9 , with value 0 in each cell#
def create_grid():
    
    matt= [[0 for row_i in range(SIZE)] for column_j in range(SIZE)] 
    for row_i in range(SIZE):
        for column_j in range(SIZE):
            matt[row_i][column_j]=0
    return matt

#return the section, anumber between 1-3#
def get_section(number):

    if(number >=0 and number<=2):
        return 0,3

    elif (number >=3 and number <=5):
        return 3,6

    else:
        return 6,9

#check if we have the same number in the box [(3*3) grid]#        
def fill_box(mat,row,column):
    
    start_row,end_row = get_section(row)
    start_column,end_column = get_section(column)
    numbers=[1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)
    count=0
    for row_i in range(start_row,end_row):
        for column_j in range(start_column,end_column):
            mat[row_i][column_j] =numbers[count]
            count+=1

def fill_all_boxes(mat):
    
    for row in range(0,SIZE,3):
        for column in range(0,SIZE,3):
            fill_box(mat,row,column)

def sorting_row(mat,row,column,sorted_mat):
    
    checked=[0,0,0,0,0,0,0,0,0]   #array that saved if the numbers appered in the row than it will changed in the array to 1 in the position of the number #
    for column_j in range(0,SIZE):
        num=mat[row][column_j]
        
        if(checked[num-1]==0):#if the number doesnt registered , so we register him #
            checked[num-1]=1
            sorted_mat[row][column_j]=1
        else:#if the number registerd we searching for unregisterd number in his box (3*3) for unregisterd number# 
    
                new_num,new_row,new_column=find_num_in_cell_to_row(mat,row,column_j,checked,num,sorted_mat)

                if(new_num==0):#if we didnt found unregisterd number we go for the first instance of the duplicated number#
                    sorted_mat[row][column_j]=1
                    #go back to the first duplicated number and try to swap him #
                    for column_j in range(0,SIZE):

                        if(mat[row][column_j]==num):#searching for the first instance of the duplicated numbers#
                            sorted_mat[row][column_j]=0 #searching for unregisterd number to swap them #
                            new_num,new_row,new_column=find_num_in_cell_to_row(mat,row,column_j,checked,num,sorted_mat)
                            

                            if(new_num!=0):
                                #sorted_mat[new_row][new_column]=2+row#
                                swap_numbers(mat,row,column_j,new_row,new_column)
                                checked[new_num-1]=1
                                sorted_mat[row][column_j]=1
                            else:
                                if(row%3!=2):
                                    PAS_row(mat,row,column_j,checked,num,sorted_mat)
                            break

                else:
                    #sorted_mat[new_row][new_column]=2+row#
                    swap_numbers(mat,row,column_j,new_row,new_column)
                    checked[new_num-1]=1
                    sorted_mat[row][column_j]=1
                    
                            
def sorting_column(mat,row,column,sorted_mat):
    
    checked=[0,0,0,0,0,0,0,0,0]   # array that saved if the numbers appered in the row than it will changed in the array to 1 in the position of the number #
    for row_i in range(0,SIZE):
        num=mat[row_i][column]

        if(checked[num-1]==0):#register the number #
            checked[num-1]=1
            if sorted_mat[row_i][column] == 0:
                sorted_mat[row_i][column]=1
        else:#if the number already registerd search for unregisterd number#
           
                new_num,new_row,new_column=find_num_in_cell_to_column(mat,row_i,column,checked,num,sorted_mat)

                if(new_num==0):
                    sorted_mat[row_i][column]=1
                #go back to the first duplicated number and try to swap him #
                    for row_i in range(0,SIZE):#searching for the duplicated instance#
                       
                        if(mat[row_i][column]==num):
                            sorted_mat[row_i][column]=0 
                            new_num,new_row,new_column=find_num_in_cell_to_column(mat,row_i,column,checked,num,sorted_mat)

                            if(new_num!=0):
                                #sorted_mat[new_row][new_column]=2+column#
                                swap_numbers(mat,row_i,column,new_row,new_column)
                                checked[new_num-1]=1
                                sorted_mat[row_i][column]=1
                            else : 
                                if (column %3 !=2):
                                    PAS_column(mat,row_i,column,checked,num,sorted_mat)
                            break
                          
                else:
                    #sorted_mat[new_row][new_column]=2+column#
                    swap_numbers(mat,row_i,column,new_row,new_column)
                    checked[new_num-1]=1
                    sorted_mat[row_i][column]=1


def find_num_in_cell_to_row(mat,row,column,checked,num,sorted_mat):
    
    starting_row,ending_row=get_section(row)
    starting_column,ending_column=get_section(column)

    for row_i in range(starting_row,ending_row):
        for column_j in range(starting_column,ending_column):

            if((sorted_mat[row_i][column_j]==0) and row_i !=row): #searchiong for unregisterd number#
                num=mat[row_i][column_j]
                if(checked[num-1]==0 ):
                    return num,row_i,column_j

    for row_i in range(row,ending_row):
        num=mat[row_i][column]
        #searching for registerd number in the column#
        if(checked[num-1]==0 ):
            return num,row_i,column
    return 0,0,0

def find_num_in_cell_to_column(mat,row,column,checked,num,sorted_mat):
    
    starting_row,ending_row=get_section(row)
    starting_column,ending_column=get_section(column)

    for column_j in range(starting_column,ending_column):
        for row_i in range(starting_row,ending_row):

            if(( sorted_mat[row_i][column_j]==0) and column !=column_j): 
                num=mat[row_i][column_j]

                if(checked[num-1]==0):
                    return num,row_i,column_j

    for column_j in range(column,ending_column):#search in the row that allready sorted#
        num=mat[row][column_j]

        if(checked[num-1]==0 ):
            return num,row,column_j
    return 0,0,0


def swap_numbers(mat,old_row,old_column,new_row,new_column):
    
    tmp=mat[old_row][old_column]
    mat[old_row][old_column]=mat[new_row][new_column]
    mat[new_row][new_column]=tmp

def PAS_row(mat,row,column,checked,num,sorted_mat):
    count = 0 
    last_column=9
    while count < 18 and checked[num-1] != 0 : 
        for column_j in range(SIZE-1):
                if(mat[row][column_j]==num and last_column !=column_j):
                    swap_numbers(mat,row,column_j,row+1,column_j)
                    sorted_mat[row][column_j]=1
                    num = mat[row][column_j]
                    last_column = column_j
                    count += 1
                    break
            
    if checked[num-1] == 0:
        checked[num-1]=1
        sorted_mat[row][column_j]=1
        return
                
    

def PAS_column(mat,row,column,checked,num,sorted_mat):
    count = 0 
    last_row = 9
    while count < 18 and checked[num-1] != 0 : 
        for row_i in range(SIZE-1):
                if(mat[row_i][column]==num and last_row !=row_i):
                    swap_numbers(mat,row_i,column,row_i,column+1)
                    checked[num-1]=1

                    num = mat[row_i][column]
                    last_row = row_i
                    count += 1
                    break
    if checked[num-1] == 0:
        checked[num-1]=1
        sorted_mat[row_i][column]=1
        return

             
          
    



def print_mat(mat):
    
    for row in range(SIZE):
        if(row%3==0):
            print("-----------------------------------------")

        for column in range(SIZE+1):

            if(column%3==0 ):
                print("||",end =" ")

            else:
                print("|",end =" ")

            if((row>=0 and row<SIZE)and (column>=0 and column<SIZE)):
                if(mat[row][column]==0 or mat[row][column]==None):
                    print(" ",end =" ")
                else:
                    print((mat[row][column]) ,end =" ")

        print(" ")
        
    print("-----------------------------------------")

def main():
    
    mat=create_grid()
    sorted_mat=create_grid()
    fill_all_boxes(mat)
    print_mat(mat)
    print("---------#############-----------")
    for i in range(9):
       print("run number :",i)
       sorting_row(mat,i,i,sorted_mat)
       sorting_column(mat,i,i,sorted_mat)
       print_mat(mat)
       print("---------#############-----------")
   



main()
