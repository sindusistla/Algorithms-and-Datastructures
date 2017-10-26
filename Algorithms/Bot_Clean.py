#!/usr/bin/python

# Head ends here
def next_move(posr, posc, board):
    # Given as input the position of bot
    # four adjacent co ordinates are (posr,posc) (posr-1,posc)(posr+1,posc) (posr,posc-1) (posr,posc+1)
    if (board[posr][posc]=="d"):
        # Dirt in current position
        print("CLEAN")
    #elif(posr-1>0):
    elif(board[posr-1][posc]=="d"):
            print("UP");
            #posr=posr-1
    elif(board[posr+1][posc]=="d"):
        print("DOWN")
        #posc=posc+1;
    elif(board[posr][posc+1]=="d"):
        print("RIGHT")
        #posc=posc+1
    #elif(posc-1>0):
    elif(board[posr][posc-1]=="d"):
            print("LEFT")
            #posc=posc-1


"""def next_move(posr,posc,board):
    if(board[posr][posc]== "d"):
        print("CLEAN");
    else:
        # Complete the current row
        if(posc<4):
            for i in range(posc,4):
                # Move Right
                print("RIGHT")
        else:
            for i in range(4-posc,0,-1):
                print("LEFT");"""

def next_move(posr,posc,board):
    # from the given position take the bot to first cell on the board


# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
