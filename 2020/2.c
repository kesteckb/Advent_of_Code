/* To try to debug the problem, they have created a list (your puzzle input) 
of passwords (according to the corrupted database) and the corporate policy 
when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy 
indicates the lowest and highest number of times a given letter must appear for 
the password to be valid. For example, 1-3 a means that the password must contain 
a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; 
it contains no instances of b, but needs at least 1. The first and third passwords 
are valid: they contain one a or nine c, both within the limits of their 
respective policies.

How many passwords are valid according to their policies? */

#include <stdio.h>
#include <stdlib.h>

#define MAX_PATH 255

typedef enum bool {false,true} bool;

void valid(int min, int max, char letter, char pw[], int *valid_1, int *valid_2);

int main(void)
{
    FILE *fptr;
    char letter;
    char buffer[MAX_PATH];
    int min;
    int max;
    int valid_1 = 0;
    int valid_2 = 0;

    /* File Handling */
    fptr = fopen("input2.txt", "r");
    if (fptr == NULL)
    {
        fprintf(stderr, "File does not exist");
        exit(EXIT_FAILURE);
    }
    
    else
    {
        while (!feof(fptr))
        {
            fscanf(fptr, "%d-%d %c: ", &min, &max, &letter);
            fgets(buffer, MAX_PATH, fptr);
            valid(min, max, letter, buffer, &valid_1, &valid_2);
        }
    }

    printf("Valid Passwords\nPart 1: %d\nPart 2: %d\n", valid_1, valid_2);

    fclose(fptr);
    return 0;
}

void valid(int min, int max, char letter, char pw[], int *valid_1, int *valid_2)
{
    int count = 0;
    int i = 0;
    
    while ((pw[i] != '\0') && (pw[i] != '\n'))
    {
        if (pw[i] == letter)
        {
            count++;
        }
        i++;
    }
    
    /* Part 1: for pw to be valid, there must be between 'min' and 
       'max' occurances of 'letter' in 'pw[]' */
    if ((count >= min) && (count <= max))
    {
        (*valid_1)++;
    }

    /* Part 2: min is pos 1, max is pos 2. One and only one of them
       must be the magic letter for the password to be valid */
    if (((pw[min - 1] == letter) && (pw[min - 1] != pw[max - 1])) || 
        ((pw[max - 1] == letter) && (pw[min - 1] != pw[max - 1])))
    {
        (*valid_2)++;
    }
}
