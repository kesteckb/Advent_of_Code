#include <stdio.h>
#include <stdlib.h>

int calculate(int mass);
int read_file(FILE* fptr);

int main(void)
{
    int mass;
    int fuel;
    FILE* fptr;

    fptr = fopen("2019_day1.txt", "r");

    fuel = read_file(fptr);
    
    printf("--%d--\n", fuel);
    
    fclose(fptr);
    return 0;
}

int calculate(int mass)
{    
    int total_fuel;
    
    int fuel = (mass/3) - 2;
    total_fuel = fuel;
    while (fuel > 0)
    {
        fuel = ((fuel/3) - 2);
        if (fuel < 0)
        {
            fuel = 0;
        }    
        total_fuel += fuel;
        printf("%d\n", fuel);
    }

    return total_fuel;
}

int read_file(FILE* fptr)
{
    int max_path = 255;
    char buffer[max_path];
    int num;

    while (fgets(buffer, max_path, fptr))
    {
        num += calculate(atoi(buffer));
    }
    return num;
}