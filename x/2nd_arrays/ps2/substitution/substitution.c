#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function prototype for the validate_key function
int validate_key(string key);

int main(int argc, string argv[])
{
    // Check for exactly 2 command-line arguments (program name and key)
    // and validate the key
    if (argc != 2 || !validate_key(argv[1]))
    {
        // Print usage message if the number of arguments or key is not valid
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string key = argv[1];

    // Prompt user for plaintext
    string plaintext = get_string("plaintext: ");

    // Start printing the ciphertext
    printf("ciphertext: ");

    // Iterate over each character in the plaintext
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        // Check if the character is alphabetic
        if (isalpha(plaintext[i]))
        {
            // Check for case and replace the plaintext character with the corresponding key character
            if (isupper(plaintext[i]))
            {
                printf("%c", toupper(key[plaintext[i] - 'A']));
            }
            else
            {
                printf("%c", tolower(key[plaintext[i] - 'a']));
            }
        }
        else
        {
            // If the character is not alphabetic, just print it as is
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
    return 0;
}

// Function to validate the key
// Checks for length, non-alphabetic characters and repeating characters
int validate_key(string key)
{
    // Check for exactly 26 characters
    if (strlen(key) != 26)
    {
        return 0;
    }

    // Initialize a repitition array to check for repeating characters
    int repeat[26] = {0};

    for (int i = 0; i < 26; i++)
    {
        // Check if the character is alphabetic
        if (!isalpha(key[i]))
        {
            return 0;
        }

        // Convert character to lower case and calculate its index in the frequency array
        int index = tolower(key[i]) - 'a';

        // Check if the character is repeating
        if (repeat[index] > 0)
        {
            return 0;
        }

        // Increment the frequency of the character
        repeat[index]++;
    }
    // If all checks passed, the key is valid
    return 1;
}