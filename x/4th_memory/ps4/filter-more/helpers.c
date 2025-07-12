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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Copy image pixels to temp
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    // Go through entire image
    RGBTRIPLE *neighbors;
    int Gx[] = {-1, 0, 1, -2, 0, 2, -1, 0, 1};
    int Gy[] = {-1, -2, -1, 0,  0,  0, 1,  2,  1};
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int array_size = 0;
            int Gx_sum[] = {0, 0, 0};
            int Gy_sum[] = {0, 0, 0};
            int kernel[] = {0, 0, 0};

            // Allocate the neighbors array
            neighbors = malloc(9 * sizeof(RGBTRIPLE));
            if (neighbors == NULL)
            {
                // Handle error
                printf("malloc NULL\n");
                free(malloc(0));
                exit(0);
            }

            // Collect neighboring pixel values
            int cnt = 0;
            for (int y = -1; y <= 1; y++)
            {
                for (int x = -1; x <= 1; x++)
                {
                    if (0 <= i + y && i + y < height && 0 <= j + x && j + x < width)
                    {
                        neighbors[cnt] = temp[i + y][j + x];
                    }

                    else
                    {
                        neighbors[cnt].rgbtRed = 0;
                        neighbors[cnt].rgbtGreen = 0;
                        neighbors[cnt].rgbtBlue = 0;
                    }

                    cnt++;
                }
            }

            // Sum the Gx and Gy values
            for (int a = 0; a < 9; a++)
            {
                Gx_sum[0] += neighbors[a].rgbtRed * Gx[a];
                Gx_sum[1] += neighbors[a].rgbtGreen * Gx[a];
                Gx_sum[2] += neighbors[a].rgbtBlue * Gx[a];
                Gy_sum[0] += neighbors[a].rgbtRed * Gy[a];
                Gy_sum[1] += neighbors[a].rgbtGreen * Gy[a];
                Gy_sum[2] += neighbors[a].rgbtBlue * Gy[a];
            }

            // Calculate kernel values
            kernel[0] = round(sqrt(Gx_sum[0] * Gx_sum[0] + (float) Gy_sum[0] * Gy_sum[0]));
            kernel[1] = round(sqrt(Gx_sum[1] * Gx_sum[1] + (float) Gy_sum[1] * Gy_sum[1]));
            kernel[2] = round(sqrt(Gx_sum[2] * Gx_sum[2] + (float) Gy_sum[2] * Gy_sum[2]));

            // Cap kernel value at 255
            for (int b = 0; b < 3; b++)
            {
                (kernel[b] > 255) ? kernel[b] = 255 : kernel[b];
            }

            // Assign kernel values for each RGB value to new image
            image[i][j].rgbtRed = kernel[0];
            image[i][j].rgbtGreen = kernel[1];
            image[i][j].rgbtBlue = kernel[2];
            free(neighbors);
        }
    }
    return;
}
