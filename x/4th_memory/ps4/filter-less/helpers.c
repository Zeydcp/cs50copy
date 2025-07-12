#include "helpers.h"
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int gray;

    // Go through entire image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            gray = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);
            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed;
    int sepiaGreen;
    int sepiaBlue;

    // Go through entire image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            (sepiaRed > 255) ? sepiaRed = 255 : sepiaRed;
            (sepiaGreen > 255) ? sepiaGreen = 255 : sepiaGreen;
            (sepiaBlue > 255) ? sepiaBlue = 255 : sepiaBlue;

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Duplicate image
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    // Assign a flipped duplicate image to new image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][width - 1 - j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE *neighbors;
    RGBTRIPLE temp[height][width];

    // Copy image pixels to temp
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    // Go through entire image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int array_size = 0;
            int sum[3] = {0, 0, 0};

            // Count in-range pixels
            for (int y = -1; y <= 1; y++)
            {
                for (int x = -1; x <= 1; x++)
                {
                    if (0 <= i + y && i + y < height && 0 <= j + x && j + x < width)
                    {
                        array_size++;
                    }
                }
            }

            // Allocate the array
            neighbors = malloc(array_size * sizeof(RGBTRIPLE));
            if (neighbors == NULL)
            {
                // Handle error
                printf("malloc NULL\n");
                free(malloc(0));
                exit(0);
            }

            // Collect pixel values
            int cnt = 0;
            for (int y = -1; y <= 1; y++)
            {
                for (int x = -1; x <= 1; x++)
                {
                    if (0 <= i + y && i + y < height && 0 <= j + x && j + x < width)
                    {
                        neighbors[cnt] = temp[i + y][j + x];
                        cnt++;
                    }
                }
            }

            // Add up all RGB values of neighbors
            for (int a = 0; a < cnt; a++)
            {
                sum[0] += neighbors[a].rgbtRed;
                sum[1] += neighbors[a].rgbtGreen;
                sum[2] += neighbors[a].rgbtBlue;
            }

            // Assign average for each RGB value to new image
            image[i][j].rgbtRed = round(sum[0] / (float) cnt);
            image[i][j].rgbtGreen = round(sum[1] / (float) cnt);
            image[i][j].rgbtBlue = round(sum[2] / (float) cnt);
            free(neighbors);
        }
    }
    return;
}
