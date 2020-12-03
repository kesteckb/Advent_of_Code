#include <stdio.h>
#include <stdlib.h>

void part_1(char facing, char turn, int blocks, int *move_x, int *move_y);

int main(void)
{
    FILE *fptr;
    char turn;
    int blocks;
    char facing;
    int move_x = 0;
    int move_y = 0;

    /* temporarily hard coded */
    facing = 'N';
    turn = 'L';
    blocks = 5;

    fptr = fopen("input1.txt", "r");

    

    part_1(facing, turn, blocks, &move_x, &move_y);

    printf("Part 1: %d blocks\n", (abs(move_x) + (abs(move_y))));

    fclose(fptr);
    return 0;
}

void part_1(char facing, char turn, int blocks, int *move_x, int *move_y)
{
    if (facing == 'N')
    {
        if (turn == 'L')
        {
            facing = 'W';
            (*move_x) -= blocks;
            return;
        }
        else if (turn == 'R')
        {
            facing = 'E';
            (*move_x) += blocks;
            return;
        }
    }
    else if (facing == 'E')
    {
        if (turn == 'L')
        {
            facing = 'N';
            (*move_y) += blocks;
            return;
        }
        else if (turn == 'R')
        {
            facing = 'S';
            (*move_y) -= blocks;
            return;
        }
    }
    else if (facing == 'S')
    {
        if (turn == 'L')
        {
            facing = 'E';
            (*move_x) += blocks;
            return;
        }
        else if (turn == 'R')
        {
            facing = 'W';
            (*move_x) -= blocks;
            return;
        }
    }
    else
    {
        if (turn == 'L')
        {
            facing = 'S';
            (*move_y) -= blocks;
            return;
        }
        else if (turn == 'R')
        {
            facing = 'N';
            (*move_y) += blocks;
            return;
        }
    }
}