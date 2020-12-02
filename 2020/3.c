/*

*/
#include <stdio.h>
#include <stdlib.h>

typedef enum bool {false,true} bool;

int main(void)
{
    FILE *fptr;


    fptr = fopen("input3.txt", "r");
    if (fptr == NULL)
    {
        fprintf(stderr, "File does not exist.\n");
        exit(EXIT_FAILURE);
    }


    fclose(fptr);
    return 0;
}