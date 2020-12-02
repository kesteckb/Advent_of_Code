/*--- Part Two ---
You notice a progress bar that jumps to 50% completion. Apparently, the door 
isn't yet satisfied, but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway 
around the circular list. That is, if your list contains 10 items, only include a digit 
in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has 
an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
What is the solution to your new captcha? */

#include <stdio.h>
#include <stdlib.h>

int find_match(int arr[], int count);
int part_2(int arr[], int count);

int main(void)
{
    FILE *fptr;
    int value;
    int count = 0;
    int arr[2500];
    int sum, new_sum;

    fptr = fopen("input1.txt", "r");
    if (fptr == NULL)
    {
        fprintf(stderr, "File does not exist\n");
    }

    else
    {
        while ((value = fgetc(fptr)) != EOF)
        {
            arr[count] = (value - '0');
            count++;
        }
        printf("\n");
    }
    sum = find_match(arr, count);
    new_sum = part_2(arr, count);

    printf("Part 1: %d\n", sum);
    printf("Part 2: %d\n", new_sum);

    return 0;
}

int part_2(int arr[], int count)
{
    int half = count / 2;
    int i;
    int sum = 0;

    for (i = 0; i < half; i++)
    {
        if (arr[i] == arr[half + i])
        {
            sum += arr[i];
        }
    }
    for (i = half; i < count; i++)
    {
        if (arr[i] == arr[i - half])
        {
            sum += arr[i];
        }
    }
    return sum;
}

int find_match(int arr[], int count)
{
    int i;
    int sum = 0; 

    for (i = 0; i < (count); i++)
    {
        if (i < (count - 1))
        {
            if (arr[i] == arr[i + 1])
            {
                sum += arr[i];
            }
        }
        else if (i == (count - 1))
        {
            if (arr[i] == arr[0])
            {
                sum += arr[i];
            }
        }
    }
    return sum;
}