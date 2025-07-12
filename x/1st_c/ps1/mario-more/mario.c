#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int Height;
    do
    {
        Height = get_int("Height: ");
    }
    while (Height < 1 || Height > 8);
    for (int i = 1; i <= Height; i++)
    {
        // Print spaces
        for (int j = 0; j < Height - i; j++)
        {
            printf(" ");
        }

        // Print left side of the pyramid
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }

        // Print spaces between the two sides
        printf("  ");

        // Print right side of the pyramid
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }

        // Move to the next line
        printf("\n");
    }
}