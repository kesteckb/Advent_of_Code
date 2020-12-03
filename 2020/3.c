#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PATH 50

typedef enum bool {false,true} bool;

void count_trees11(char trees[], int row, int *conflicts);
void count_trees31(char trees[], int row, int *conflicts);
void count_trees51(char trees[], int row, int *conflicts);
void count_trees71(char trees[], int row, int *conflicts);
void count_trees12(char trees[], int row, int *conflicts);

int main(void)
{
    FILE *fptr;
    char buffer[MAX_PATH];
    int trees11 = 0;
    int trees31 = 0;
    int trees51 = 0;
    int trees71 = 0;
    int trees12 = 0;
    int count = 0;
    unsigned long total;


    fptr = fopen("input3.txt", "r");
    if (fptr == NULL)
    {
        fprintf(stderr, "File does not exist.\n");
        exit(EXIT_FAILURE);
    }

    while (fgets(buffer, MAX_PATH, fptr))
    {
        count_trees11(buffer, count, &trees11);
        count_trees31(buffer, count, &trees31);
        count_trees51(buffer, count, &trees51);
        count_trees71(buffer, count, &trees71);
        count_trees12(buffer, count, &trees12);
        count++;
    }
    total = (unsigned long)trees11 * (unsigned long)trees31 *
        (unsigned long)trees51 * (unsigned long)trees71 * (unsigned long)trees12;

    printf("Part 1: %d\nPart 2: %ld\n", trees31, total);
    fclose(fptr);
    return 0;
}

void count_trees31(char trees[], int row, int *conflicts)
{
    if (trees[(3 * row) % 31] == '#')
    {
        (*conflicts)++;
    }
}

void count_trees11(char trees[], int row, int *conflicts)
{
    if (trees[(row) % 31] == '#')
    {
        (*conflicts)++;
    }
}

void count_trees51(char trees[], int row, int *conflicts)
{
    if (trees[(5 * row) % 31] == '#')
    {
        (*conflicts)++;
    }
}

void count_trees71(char trees[], int row, int *conflicts)
{
    if (trees[(7 * row) % 31] == '#')
    {
        (*conflicts)++;
    }
}

void count_trees12(char trees[], int row, int *conflicts)
{
    if (row % 2 == 0)
    {
        if (trees[(row/2) % 31] == '#')
        {
            (*conflicts)++;
        }
    }
}