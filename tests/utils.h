#define CREATE_BUF                 \
char buf[1024];                    \
FILE *f = fopen(argv[1], "rb");    \
size_t n = fread(buf, 1, 1023, f); \
buf[n] = '\0';                     \
fclose(f)
