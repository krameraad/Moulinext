#pragma once

#include <string.h>
#include <stdio.h>
#include <ctype.h>

#define CREATE_BUF                 \
char buf[1024];                    \
FILE *f = fopen(argv[1], "rb");    \
size_t n = fread(buf, 1, 1023, f); \
buf[n] = '\0';                     \
fclose(f)

#define CREATE_CTYPE(x)                        \
int main(int argc, char const *argv[])         \
{                                              \
    int expected;                              \
    int received;                              \
                                               \
    CREATE_BUF;                                \
    if (buf[0] == 1)                           \
        if (!ft_is##x(0) != !is##x(0))         \
            return 1;                          \
    for (size_t i = 0; buf[i]; ++i)            \
    {                                          \
        expected = !is##x(buf[i]);             \
        received = !ft_is##x(buf[i]);          \
        if (expected != received)              \
            return 1;                          \
    }                                          \
    return 0;                                  \
}
