#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

float calc_hours(int hours[], int weeks, char output);

int main(void)
{
    int weeks = get_int("Number of weeks taking CS50: ");
    int hours[weeks];

    for (int i = 0; i < weeks; i++)
    {
        hours[i] = get_int("Week %i HW Hours: ", i);
    }

    char output;
    do
    {
        output = toupper(get_char("Enter T for total hours, A for average hours per week: "));
    }
    while (output != 'T' && output != 'A');

    printf("%.1f hours\n", calc_hours(hours, weeks, output));
}

// TODO: complete the calc_hours function
float calc_hours(int hours[], int weeks, char output)
{
    // Initialize total hours to 0
    int total_hours = 0;
    // Sum up the hours for each week
    for (int i = 0; i < weeks; i++)
    {
        total_hours += hours[i];
    }

    // If the user chose 'T', return the total hours
    if (output == 'T')
    {
        return total_hours;
    }

    // If the user chose 'A', return the average hours per week
    else if (output == 'A')
    {
        return (float) total_hours / weeks;
    }

    // Default return statement. In this program, this line would never be executed
    // as we ensure the output to be either 'T' or 'A' in the main function
    return 0.0;
}