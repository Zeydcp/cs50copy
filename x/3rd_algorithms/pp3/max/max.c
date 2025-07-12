// Practice writing a function to find a max value

#include <cs50.h>
#include <stdio.h>

int max(int array[], int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number of elements: ");
    }
    while (n < 1);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        arr[i] = get_int("Element %i: ", i);
    }

    printf("The max value is %i.\n", max(arr, n));
}

// TODO: return the max value
int max(int array[], int n)
{
    // Assume the first element as the maximum value
    int maxValue = array[0];

    // Iterate through the array to find the maximum value
    for (int i = 1; i < n; i++)
    {
        // Compare the current element with the maximum value
        // If the current element is greater, update the maximum value
        if (array[i] > maxValue)
        {
            maxValue = array[i];
        }
    }

    // Return the maximum value
    return maxValue;
}