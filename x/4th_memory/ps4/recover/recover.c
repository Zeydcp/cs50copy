#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];

    // Remember filenames
    char *infile = argv[1];
    char *outfile = malloc(sizeof(BYTE) * 8);

    // Open memory card
    FILE *raw_file = fopen(infile, "r");
    if (raw_file == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 2;
    }

    int cnt = 0;
    sprintf(outfile, "%03i.jpg", cnt);

    // Open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(raw_file);
        printf("Could not create %s.\n", outfile);
        return 3;
    }

    // Repeat until end of card
    // Read 512 bytes into a buffer
    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, raw_file) == BLOCK_SIZE)
    {
        // If start of new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If first JPEG
            if (cnt == 0)
            {
                cnt++;
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, outptr);
            }

            else
            {
                // Close old JPEG and open a new one
                free(outfile);
                fclose(outptr);
                outfile = malloc(sizeof(BYTE) * 8);
                sprintf(outfile, "%03i.jpg", cnt);
                outptr = fopen(outfile, "w");
                cnt++;
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, outptr);
            }
        }

        // Continue writing to current JPEG
        else
        {
            if (cnt > 0)
            {
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, outptr);
            }
        }
    }

    // Free the remaining allocated memory
    fclose(raw_file);
    fclose(outptr);
    free(outfile);
}