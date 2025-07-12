// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 193336;

int _size = 0;

// Hash table
node *table[N] = {NULL};

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *traverse = table[index];
    while (traverse)
    {
        if (!strcasecmp(traverse->word, word))
        {
            return true;
        }

        traverse = traverse->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int n = strlen(word);
    char char_copy[3];
    char_copy[0] = (isalpha(word[0])) ? word[0] : 'A';
    char_copy[1] = (isalpha(word[n / 2])) ? word[n / 2] : 'A';
    char_copy[2] = (isalpha(word[n - 1])) ? word[n - 1] : 'A';

    if (n < 5)
    {
        return 11 * (676 * toupper(char_copy[0]) + 26 * toupper(char_copy[1]) + toupper(char_copy[2]) - 703 * 'A');
    }

    else if (n > 13)
    {
        return 11 * (676 * toupper(char_copy[0]) + 26 * toupper(char_copy[1]) + toupper(char_copy[2]) - 703 * 'A') + 10;
    }

    else
    {
        return 11 * (676 * toupper(char_copy[0]) + 26 * toupper(char_copy[1]) + toupper(char_copy[2]) - 703 * 'A') + n - 4;
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (!file)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }

    char word[LENGTH + 1];
    while (fscanf(file, "%s", word) != EOF)
    {
        node *new = malloc(sizeof(node));
        if (!new)
        {
            fclose(file);
            printf("Could not allocate memory to node.\n");
            return false;
        }

        strcpy(new->word, word);
        unsigned int index = hash(new->word);
        new->next = table[index];
        table[index] = new;
        _size++;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return _size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i], *tmp = table[i];
        while (cursor)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }

    return true;
}
