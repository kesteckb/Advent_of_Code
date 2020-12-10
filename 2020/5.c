/* --- Day 5: Binary Boarding ---
You board your plane only to discover a new problem: you dropped your boarding 
pass! You aren't sure which seat is yours, and all of the flight attendants are 
busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby 
boarding passes (your puzzle input); perhaps you can find your seat through 
process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat 
people. A seat might be specified like FBFBBFFRLR, where F means "front", B 
means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 
128 rows on the plane (numbered 0 through 127). Each letter tells you which half 
of a region the given seat is in. Start with the whole list of rows; the first 
letter indicates whether the seat is in the front (0 through 63) or the back (64 
through 127). The next letter indicates which half of that region the seat is in, 
and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of 
the 8 columns of seats on the plane (numbered 0 through 7). The same process 
as above proceeds again, this time with only three steps. L means to keep the 
lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. 
In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the 
highest seat ID on a boarding pass? */

#include <stdio.h>
#include <stdlib.h>

#define NUM_ROWS 128
#define NUM_COLS 8
#define R_STEPS 7
#define C_STEPS 3
#define MAX_PATH 100

typedef enum bool {false,true} bool;

void init_grid(bool* grid);
void init_rows(int rows[], int num);
int search(char pass[], int rows, int start, int r_steps);

int main(void)
{
    FILE *fptr;
    char pass[MAX_PATH];
    int rows[NUM_ROWS];
    int seats[NUM_COLS];
    int row, column, seatID, seatID2;
    int high = 0;
    bool grid[NUM_ROWS][NUM_COLS];
    int i, j;

    init_rows(rows, NUM_ROWS);
    init_rows(seats, NUM_COLS);
    init_grid(&grid[0][0]);

    fptr = fopen("input5.txt", "r");
    if (fptr == NULL)
    {
        fprintf(stderr, "File does not exist.\n");
        exit(EXIT_FAILURE);
    }

    while (fgets(pass, MAX_PATH, fptr))
    {
            pass[10] = '\0';
            row = search(pass, NUM_ROWS, 0, R_STEPS);  
            column = search(pass, NUM_COLS, 7, C_STEPS);
            grid[row][column] = true;
            seatID = (row * 8) + column;

        if (seatID > high)
        {
            high = seatID;
        }
    }

    for (i = 0; i < NUM_ROWS; i++)
    {
        for (j = 1; j < NUM_COLS - 1; j++)
        {
            if ((grid[i][j] == false) && (grid[i][j-1] == true) && (grid[i][j+1] == true))
            {
                seatID2 = (i*8)+j;
            }
        }
    }

    printf("Part 1: %d\n", high);
    printf("Part 2: %d\n", seatID2);
    fclose(fptr);
    return 0;
}

void init_rows(int rows[], int num)
{
    int i;

    for (i = 0; i < num; i++)
    {
        rows[i] = i;
    }
}

void init_grid(bool* grid)
{
    int position;

    for (position = 0; position < NUM_ROWS*NUM_COLS; position++)
    {
        grid[position] = false;
    }
}

int search(char pass[], int rows, int start, int r_steps)
{
    int m, i;
    int l = 0;
    int r = rows - 1;
    
    for (i = 0; i < (r_steps - 1); i++)
    {
        m = (l + r) / 2;
        
        if ((pass[i + start] == 'F') || (pass[i + start] == 'L'))
        {
            r = m;
        }
        else if ((pass[i + start] == 'B') || (pass[i + start] == 'R'))
        {
            l = m + 1;
        }
    }
    if ((pass[start + r_steps - 1] == 'F') || (pass[start + r_steps - 1] == 'L'))
    {
        return l;
    }
    else
    {
        return r;
    }
}