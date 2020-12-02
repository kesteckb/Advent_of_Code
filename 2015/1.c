#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fptr;
    char paren;
    int floor = 0;
    int position;

    fptr = fopen("input1.txt", "r");

    if (fptr == NULL)
    {
        fprintf(stderr, "File is not available\n");
    }
    else
    {
        while((paren = fgetc(fptr)) != EOF)
        {
            if (paren == '(')
            {
                floor++;
            }
            else if (paren == ')')
            {
                floor--;
            }
            position++;
            if(floor == -1)
            {
                printf("Position: %d\n", position);
            }
        }
    }

    printf("--floor: %d--\n", floor);

    fclose(fptr);
    return 0;
}