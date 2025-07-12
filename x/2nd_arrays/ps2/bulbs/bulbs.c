#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string input = get_string("Enter your message: ");
    int length = strlen(input);

    // Loop through every character
    for (int i = 0; i < length; i++)
    {
        // Create array that stores bits
        int byte[BITS_IN_BYTE] = {0};
        int bit = 7;

        // Convert characters to bits
        while (input[i] > 0)
        {
            byte[bit--] = input[i] % 2;
            input[i] /= 2;
        }

        // Print bits
        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            print_bulb(byte[j]);
        }

        // New for each character
        printf("\n");
    }

}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
