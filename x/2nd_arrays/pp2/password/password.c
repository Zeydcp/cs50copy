// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol!\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    // Initialize flags for each type of character
    bool has_lowercase = false, has_uppercase = false, has_digit = false, has_symbol = false;

    // Iterate over each character in the string
    for (int i = 0, n = strlen(password); i < n; i++)
    {
        // Check each character type
        if (islower(password[i]))
        {
            has_lowercase = true;
        }

        else if (isupper(password[i]))
        {
            has_uppercase = true;
        }

        else if (isdigit(password[i]))
        {
            has_digit = true;
        }

        else if (ispunct(password[i]))
        {
            has_symbol = true;
        }
    }

    // Return whether the password meets all criteria
    return has_lowercase && has_uppercase && has_digit && has_symbol;
}
