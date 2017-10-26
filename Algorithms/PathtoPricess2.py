#
def nextMove(n,bot_row,bot_col,grid,pri_row,pri_col):
    # r,c is position of the bot
    # find the position of the pricess
    # Compute the difference
    # if row_difference is +ve Bot should go up , if -ve bot should go down
    direction=""
    row_difference=bot_row-pri_row;
    #if col_difference is +ve , bot should go left, -ve bot should go right
    col_difference=bot_col-pri_col;

    while True:
        if (row_difference == 0):
            # On same row
            if(col_difference >0):
                # Bot go left
                direction = "LEFT";
            else:
                direction="RIGHT"
            break;
        if (col_difference == 0):
            # On same col
            if(row_difference > 0):
                direction="UP"
            else:
                direction="DOWN"
            break;

        if (abs(row_difference)> abs(col_difference)):
            # Decide between left or right
            if (col_difference > 0):
                direction="LEFT";
                break;
            else:
                direction="RIGHT";
                break;
        elif (abs(row_difference)< abs(col_difference)):
            # Decide between up and down
            if(row_difference > 0):
                direction="UP"
                break;
            else:
                direction="DOWN"
                break;
        elif (abs(row_difference)== abs(col_difference)) :
            if (row_difference > 0):
                direction = "UP"
                break;
            else:
                direction = "DOWN"
                break;
    return direction;



n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    a=input()
    grid.append(a)
    if ("p" in a):
        # Position of the pricess
        a_p=i;
        b_p=a.index("p")
        #print(a_p,b_p)


print(nextMove(n,r,c,grid, a_p,b_p))
