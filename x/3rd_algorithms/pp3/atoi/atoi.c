#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // TODO
    // Base case: when the string is empty, return 0
    if (strlen(input) == 0)
    {
        return 0;
    }

    // Get the index of the last character in the string
    int lastIdx = strlen(input) - 1;

    // Convert the last character into its numeric value
    int lastDigit = input[lastIdx] - '0';

    // Create a new shortened string by moving the null terminator
    // one position to the left
    input[lastIdx] = '\0';

    // Recursive call with the shortened string
    int recursiveResult = convert(input);

    // Calculate and return the final result
    return (recursiveResult * 10) + lastDigit;
}