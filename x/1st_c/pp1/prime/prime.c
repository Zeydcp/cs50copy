#include <cs50.h>
#include <stdio.h>

bool prime(int number);

int main(void)
{
    int min;

    // asks user for range of values
    do
    {
        min = get_int("Minimum: ");
    }
    while (min < 1);

    int max;
    do
    {
        max = get_int("Maximum: ");
    }
    while (min >= max);

    // prints if number is prime
    for (int i = min; i <= max; i++)
    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

//  checks if number is prime
bool prime(int number)
{
    // TODO
    for (int i = 2; i < number; i++)
    {
        if ((number % i) == 0)
        {
            return false;
        }
    }
    return true;
}