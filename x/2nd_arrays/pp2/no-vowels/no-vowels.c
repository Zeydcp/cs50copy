// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function prototype
string replace(string input);

int main(int argc, string argv[])
{
    // Check if the number of arguments is exactly 2
    if (argc != 2)
    {
        printf("Usage: ./no-vowels word\n");
        return 1;
    }

    // Call the replace function and print the result
    printf("%s\n", replace(argv[1]));
    return 0;
}

// Function to replace vowels with specific numbers
string replace(string input)
{
    // Loop through each character of the string
    for (int i = 0, n = strlen(input); i < n; i++)
    {
        // Convert the character to lowercase for case-insensitive comparison
        char lower = tolower(input[i]);
        switch (lower)
        {
            case 'a':
                input[i] = '6';
                break;
            case 'e':
                input[i] = '3';
                break;
            case 'i':
                input[i] = '1';
                break;
            case 'o':
                input[i] = '0';
                break;
        }
    }
    return input;
}
