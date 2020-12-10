#include <stdio.h>

#define QUEUE_SIZE 1000;

typedef enum bool {false,true} bool;

typedef struct passport {
    bool byr;
    bool iyr;
    bool eyr;
    bool hgt;
    bool hcl;
    bool ecl;
    bool pid;
    bool cid;
} Passport;

typedef struct queue {
    Passport list[QUEUE_SIZE];
    int front;
    int back;
} Queue;

int main(void)
{
    FILE *fptr;
    Queue queue;
    Passport passport;
    queue.front = 0;
    queue.back = 1;


    fptr = fopen("input4.txt", "r");
    if (fptr == NULL)
    {
        fprintf(stderr, "File does not exist.\n");
        exit(EXIT_FAILURE);
    }


    return 0;
}

