#include "../libft.h"
#include "../utils.h"
#include <string.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
    if (argc == 1)
        return ft_strlen(NULL), 0;
    CREATE_BUF;

    return ft_strlen(buf) != strlen(buf);
}
