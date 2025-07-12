#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Function prototype for the only_digits function
bool only_digits(string s);

// Function prototype for the rotate function
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // Check for exactly 2 command-line arguments (program name and key)
    // and validate the key
    if (argc != 2 || !only_digits(argv[1]))
    {
        // Print usage message if the number of arguments or key is not valid
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);
    string plaintext = get_string("plaintext:  ");
    printf("ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        printf("%c", rotate(plaintext[i], key));
    }

    printf("\n");
    return 0;
}

// Function to check if the string contains digits exclusively
bool only_digits(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

// Function that rotates characters by n
char rotate(char c, int n)
{
    if (isalpha(c))
    {
        if (isupper(c))
        {
            c -= 'A';
            c = (c + n) % 26;
            c += 'A';
        }

        else
        {
            c -= 'a';
            c = (c + n) % 26;
            c += 'a';
        }
    }

    return c;
}