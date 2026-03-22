#include "../libft.h"
#include "../utils.h"

int main(int argc, char const *argv[])
{
    int expected;
    int received;

    CREATE_BUF;
    if (buf[0] == 1)
        if (!!ft_isalpha(0) != !!isalpha(0))
            return 1;
    for (size_t i = 0; buf[i]; ++i)
    {
        expected = !!isalpha(buf[i]);
        received = !!ft_isalpha(buf[i]);
        if (expected != received)
            return 1;
    }
    return 0;
}
