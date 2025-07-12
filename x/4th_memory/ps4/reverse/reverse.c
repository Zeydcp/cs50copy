#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    int length = strlen(argv[1]);
    if (strcmp(argv[1] + length - 4, ".wav"))
    {
        printf("Input is not a WAV file.\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, input);
    long first_position = ftell(input);

    // Use check_format to ensure WAV format
    // TODO #4
    bool wav = check_format(header);

    // Open output file for writing
    // TODO #5
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(&header, sizeof(WAVHEADER), 1, output);

    // Use get_block_size to calculate size of block
    // TODO #7
    long block_size = get_block_size(header);

    // Write reversed audio to file
    // TODO #8
    fseek(input, -block_size, SEEK_END);
    long new_position;
    do
    {
        long buffer;
        fread(&buffer, block_size, 1, input);
        fwrite(&buffer, block_size, 1, output);
        fseek(input, -2 * block_size, SEEK_CUR);
        new_position = ftell(input);
    }
    while (new_position >= first_position);

    fclose(input);
    fclose(output);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        return 1;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return round(header.numChannels * header.bitsPerSample / 8.0);
}