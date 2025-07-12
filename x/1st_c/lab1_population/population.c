#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start, end;
    // TODO: Prompt for start size
    do
    {
        start = get_int("What is start size? ");
    }
    while (start < 9);

    // TODO: Prompt for end size
    do
    {
        end = get_int("What is end size? ");
    }
    while (end < start);

    // TODO: Calculate number of years until we reach threshold
    int n = 0;
    while (start < end)
    {
        start = start + (start / 3) - (start / 4);
        n++;
    }


    // TODO: Print number of years
    printf("Years: %i\n", n);
}
