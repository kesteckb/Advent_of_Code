/* After feeling like you've been falling for a few minutes, you look at the 
device's tiny screen. "Error: Device must be calibrated before first use. 
Frequency drift detected. Cannot maintain destination lock." Below the message,
 the device shows a sequence of changes in frequency (your puzzle input). A 
 value like +6 means the current frequency increases by 6; a value like -3 
 means the current frequency decreases by 3.

For example, if the device displays frequency changes of +1, -2, +3, +1, then 
starting from a frequency of zero, the following changes would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.

Here are other example situations:

+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6
Starting with a frequency of zero, what is the resulting frequency after all of 
the changes in frequency have been applied?

Your puzzle answer was 411.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
You notice that the device repeats the same frequency change list over and over.
To calibrate the device, you need to find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
(At this point, the device continues from the start of the list.)
Current frequency  3, change of +1; resulting frequency  4.
Current frequency  4, change of -2; resulting frequency  2, which has already been seen.
In this example, the first frequency reached twice is 2. Note that your device might 
need to repeat its list of frequency changes many times before a duplicate frequency 
is found, and that duplicates might be found while in the middle of processing the list.

Here are other examples:

+1, -1 first reaches 0 twice.
+3, +3, +4, -2, -4 first reaches 10 twice.
-6, +3, +8, +5, -6 first reaches 5 twice.
+7, +7, -2, -7, -4 first reaches 14 twice.
What is the first frequency your device reaches twice? */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ARR_SIZE 1000
#define MAX_PATH 15
#define HIST_LEN 150000

void sum_freq_changes(int value, int *sum);
int repeated(int change_arr[], int count);

int main(void)
{
    FILE *fptr;
    int sum = 0;
    int count = 0;
    int value, len, i, first_repeated;
    char *num_str;
    char buffer[MAX_PATH];
    int change_arr[ARR_SIZE];

    fptr = fopen("input1.txt", "r");
    if (fptr == NULL)
    {
        fprintf(stderr, "File does not exist\n");
        exit(EXIT_FAILURE);
    }

    while (!feof(fptr))
    {
        /* store each line in string: buffer */
        if (!fgets(buffer, MAX_PATH, fptr))
        {
            break;
        }

        /* get the length of the string, and malloc space for a 
           string to hold the number without the sign */
        len = strlen(buffer);
        num_str = (char*) malloc((len + 1)* sizeof(char));

        /* Move the numerals from the line in file to a temporary
           string called num_str, and end it with a '\0' value */
        for (i = 1; i < len; i++)
        {
            num_str[i - 1] = buffer[i];
        }
        num_str[len] = '\0';
        /* convert from string to integer */
        value = atoi(num_str);

        free(num_str);

        if (buffer[0] == '-')
        {
            value *= -1;
        }
        change_arr[count] = value;
        count++;
        sum_freq_changes(value, &sum);
    }
    

    first_repeated = repeated(change_arr, count);
    
    printf("Part 1: %d\nPart 2: %d\n", sum, first_repeated);

    fclose(fptr);
    return 0;
}

void sum_freq_changes(int value, int *sum)
{
    (*sum) += value;
}

/* This is a terribly innefficient way to do this :(
   It took 132,085 frequency changes to have a frequency
   repeat */
int repeated(int change_arr[], int count)
{
    int i = 0;
    int j;
    int length = 0;
    int frequency = 0;
    int history[HIST_LEN];
    do 
    {
        if ((i == count))
        {
            i = 0;
        }
        frequency += change_arr[i];
        history[length] = frequency;
        if (length > 0)
        {
            for (j = 0; j < length; j++)
            {
                if (history[j] == frequency)
                {
                    return frequency;
                }
            }
        }
        i++;
        length++;
    } while (length < HIST_LEN);
    return 0;
}