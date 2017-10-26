#!/usr/bin/python

def PrintOutput(FirstDirection,SecondDirection,SizeofGrid):
    #print("Here",FirstDirection,SecondDirection,int(SizeofGrid/2))
    for i in range(0,int(SizeofGrid/2)):
        print(FirstDirection);
    for i in range(0,int(SizeofGrid/2)):
        print(SecondDirection);


def displayPathtoPrincess(n,grid):
    #print all the moves here
    m = int(input())
    for i in range(0, m):
        grid.append(input().strip())

    quadrant=0;
    # Find the princess
    # Check all the four corners
    #print(grid[0][0],grid[0][m+1],grid[m-1][0],grid[m-1][m+1])
    #print(grid,grid[2][2])
    if (grid[0][0]== "p"):
        # Pricess found in first quandrant
        row_intercept=0
        col_intercept=0;
        PrintOutput("UP","LEFT",m)
        quadrant=1;
    elif (grid[0][m-1]=="p"):
        # Pricess found in second quandrant
        row_intercept=0
        col_intercept=m;
        PrintOutput("UP","RIGHT")
        quadrant=2;
    elif (grid[m-1][0] == "p"):
        # Pricess found in third quadrant
        row_intercept=m
        col_intercept=0
        quadrant=3;
        PrintOutput("DOWN","LEFT",m)
    elif (grid[m-1][m-1]=="p"):
        # Princess found in fourth quadrant
        row_intercept = m
        col_intercept = m
        quadrant=4;
        PrintOutput("DOWN", "RIGHT", m)

    else:
        # Pricesess not found
        return

    # Now the pricess is found



m=0
grid=[];
displayPathtoPrincess(m,grid)
