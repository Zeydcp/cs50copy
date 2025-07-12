#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //asks for name
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}