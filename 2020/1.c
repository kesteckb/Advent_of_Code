#include <stdio.h>
#include <stdlib.h>

#define MAX_PATH 255

int main(void)
{
    FILE* fptr;
    int account[1000];
    char buffer[MAX_PATH];
    int i = 0;
    int count = 0;
    int j, k;

    fptr = fopen("day1_input.txt", "r");
    while (fgets(buffer, MAX_PATH, fptr))
    {
        account[i] = atoi(buffer);
        i++;
        count++;
    }

    for (i = 0; i < count; i++)
    {
        for (j = 0; j < count; j++)
        {
            for (k = 0; k < count; k++)
            {
                if (account[i] + account[j] + account[k]== 2020)
                {
                    printf("--%d--\n", account[i]*account[j]*account[k]);
                    printf("%d, %d, %d\n", account[i], account[j], account[k]);
                }
            }
            
        }
    }

    fclose(fptr);
    return 0;
}