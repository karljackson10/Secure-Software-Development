#include <stdio.h>

int main(int argc, char **argv)
{
    char buf[2];             // buffer for eight characters
    printf("Enter name: ");
    gets(buf);               // read from stdio (sensitive function!)
    printf("%s\n", buf);     // print out data stored in buf
    return 0;                // 0 as return value
}