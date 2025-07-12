#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int sum = 0, currentDigit;
    bool checksum;
    long Number, temp1, temp2;

    do
    {
        Number = temp2 = get_long("Number: ");
    }
    while (Number < 0);

    temp1 = Number / 10;

    //sums products' digits
    while (temp1 != 0)
    {
        currentDigit = temp1 % 10;  // Extract the last digit
        if (currentDigit > 4)
        {
            int temp4 = 2 * currentDigit;
            while (temp4 != 0)
            {
                currentDigit = temp4 % 10;  // Extract the last digit
                sum += currentDigit;  // Add the digit to the sum
                temp4 /= 10;  // Remove the last digit from the value
            }
        }
        else
        {
            sum += 2 * currentDigit;  // Add the digit to the sum
        }
        temp1 /= 100;  // Remove the last two digits from the value
    }

    //sums digits that weren't multiplied by 2
    while (temp2 != 0)
    {
        currentDigit = temp2 % 10;
        sum += currentDigit;
        temp2 /= 100;
    }

    checksum = sum % 10 == 0 ? 1 : 0;

    if (!checksum)
    {
        printf("INVALID\n");
    }
    else
    {
        int NumberLength = 0;
        long temp3 = Number;

        //calculates number of digits
        while (temp3 != 0)
        {
            temp3 /= 10;
            NumberLength++;
        }
        switch (NumberLength)
        {
            //checks if 13 digits
            case 13:
            {
                long divisor = 1;
                for (int i = 0; i < 12; i++)
                {
                    divisor *= 10;
                }
                int firstDigit = (Number / divisor) % 10;
                firstDigit == 4 ? printf("VISA\n") : printf("INVALID\n");
                break;
            }
            //checks if 15 digits
            case 15:
            {
                long divisor = 1;
                //checks if firstTwo digits matches amex
                for (int i = 0; i < 13; i++)
                {
                    divisor *= 10;
                }
                int firstTwo = (Number / divisor) % 100;
                (firstTwo == 34 || firstTwo == 37) ? printf("AMEX\n") : printf("INVALID\n");
                break;
            }
            //checks if 16 digits
            case 16:
            {
                bool checkvisa = 0;
                long divisor = 1;
                //checks if firstTwo digits matches mastercard
                for (int i = 0; i < 14; i++)
                {
                    divisor *= 10;
                }
                int firstTwo = (Number / divisor) % 100;
                if (firstTwo > 50 && firstTwo < 56)
                {
                    printf("MASTERCARD\n");
                    break;
                }
                else
                {
                    checkvisa = 1;
                }
                //checks if firstDigit matches visa
                int firstDigit = (firstTwo / 10) % 10;
                checkvisa ? (firstDigit == 4 ? printf("VISA\n") : printf("INVALID\n")) : printf("INVALID\n");
                break;
            }
            //if none of those return INVALID
            default:
                printf("INVALID\n");
                break;
        }
    }
}