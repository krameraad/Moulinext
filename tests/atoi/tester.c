#include "../libft.h"
#include "../utils.h"

int main(int argc, char const *argv[])
{
    if (argc == 1)
        return ft_atoi(NULL), 0;

    CREATE_BUF;
    if (ft_atoi(buf) != atoi(buf))
        return 1;
    return 0;
}
