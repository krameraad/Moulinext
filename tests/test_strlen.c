#include "libft.h"
#include <string.h>

#define TEST(x) result |= (strlen(x) == ft_strlen(x) << pos); ++pos

int main()
{
    int pos = 0;
    int result = 0;

    TEST("aaaa");
    TEST("aa\naa");
    TEST("");
    TEST("aa\0aa");

    return result;
}
