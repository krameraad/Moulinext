#ifndef LIBFT_H
# define LIBFT_H

# include <unistd.h>
# include <stdlib.h>

typedef struct s_list
{
	void			*content;
	struct s_list	*next;
}	t_list;

/*
PART 1
*/

/* Checks if character `c` is alphabetical.
@param c Character to test.
@return `1` if alphabetical, otherwise `0`. */
int		ft_isalpha(int c);

/* Checks if character `c` is numeric.
@param c Character to test.
@return `1` if numeric, otherwise `0`. */
int		ft_isdigit(int c);

/* Checks if character `c` is alphanumeric.
@param c Character to test.
@return `1` if alphanumeric, otherwise `0`. */
int		ft_isalnum(int c);

/* Checks if character `c` is ASCII.
@param c Character to test.
@return `1` if ASCII, otherwise `0`. */
int		ft_isascii(int c);

/* Checks if character `c` is printable.
@param c Character to test.
@return `1` if printable, otherwise `0`. */
int		ft_isprint(int c);

/* Finds the length of string `s`.
The length is the number of characters,
not including the NUL-terminator.
@param s String to get the length of.
@return Length of string `s`. */
size_t	ft_strlen(const char *s);

/* Writes `n` bytes of memory containing `c`
to the area pointed to by `s`.
@param s Area to set.
@param c Character to write.
@param n Number of bytes to write.
@return Pointer to the memory area `s`. */
void	*ft_memset(void *s, int c, size_t n);

/* Writes `n` bytes of memory containing zeros (`'\0'`)
to the area pointed to by `s`.
@param s Area to erase.
@param n Number of bytes to write. */
void	ft_bzero(void *s, size_t n);

/* Writes `n` bytes of memory from `src`
to the area pointed to by `dest`.
This function produces undefined behavior if
the memory areas overlap.
@param dest Area to write to.
@param src Area to copy from.
@param n Number of bytes to write.
@return Pointer to the memory area `dest`. */
void	*ft_memcpy(void *dest, const void *src, size_t n);

/* Writes `n` bytes of memory from `src`
to the area pointed to by `dest`.
Unlike `memcpy()`, this function behaves correctly
in the case of overlapping memory areas.
@param dest Area to write to.
@param src Area to copy from.
@param n Number of bytes to write.
@return Pointer to the memory area `dest`. */
void	*ft_memmove(void *dest, const void *src, size_t n);

/* Copies up to `size - 1` characters
from the NUL-terminated string `src` to `dst`, 
NUL-terminating the result.
@param dst String to copy to.
@param src String to copy from.
@param size How many characters to copy.
@return Total length of the string they tried to create. */
size_t	ft_strlcpy(char *dst, const char *src, size_t size);

/* Appends the NUL-terminated string `src` to the end of `dst`.
It will append at most `size - strlen(dst) - 1` bytes,
NUL-terminating the result.
@param dst String to concatenate onto.
@param src String to concatenate.
@param size How many characters to concatenate.
@return Total length of the string they tried to create. */
size_t	ft_strlcat(char *dst, const char *src, size_t size);

/* Makes `c` uppercase, if possible.
@param c Character to make uppercase.
@return `c`, whether it was changed or not. */
int		ft_toupper(int c);

/* Makes `c` lowercase, if possible.
@param c Character to make lowercase.
@return `c`, whether it was changed or not. */
int		ft_tolower(int c);

/* Finds character `c` inside string `s`.
The terminating null byte is considered part of the string,
so that if `c` is specified as `'\0'`,
this function returns a pointer to the terminator.
@param s String to search in.
@param c Character to find.
@return Pointer to the first occurrence of the character `c`
in the string `s`. `NULL` if the character is not found. */
char	*ft_strchr(const char *s, int c);

/* Finds character `c` inside string `s`, starting from the end.
The terminating null byte is considered part of the string,
so that if `c` is specified as `'\0'`,
this function returns a pointer to the terminator.
@param s String to search.
@param c Character to find.
@return Pointer to the last occurrence of the character `c`
in the string `s`. `NULL` if the character is not found. */
char	*ft_strrchr(const char *s, int c);

/* Compares up to `n` characters between
the strings `s1` and `s2`,
returning the difference.
@param s1 First string.
@param s2 Second string.
@param n How many characters to compare.
@return `0` if the strings are the same. Otherwise,
returns the difference between the first non-equal characters. */
int		ft_strncmp(const char *s1, const char *s2, size_t n);

/* Finds the first instance of `c` inside memory area `s`.
@param s Area to search.
@param c Character to find.
@param n Number of bytes to search.
@return Pointer to the first occurrence of the character `c`
in area `s`. `NULL` if the character is not found. */
void	*ft_memchr(const void *s, int c, size_t n);

/* Compares up to `n` bytes between 
the memory areas `s1` and `s2`,
returning the difference.
@param s1 First memory area.
@param s2 Second memory area.
@param n How many bytes to compare.
@return `0` if the areas are the same. Otherwise,
returns the difference between the first non-equal bytes. */
int		ft_memcmp(const void *s1, const void *s2, size_t n);

/* Locates the first occurrence of the
NUL-terminated string `little` in the string `big`,
where not more than `len` characters are searched.
Characters that appear after a `'\0'` character are not searched.
@param big String to search in.
@param little String to find.
@param len Amount of characters to check.
@return If `little` is empty, `big` is returned;
if little occurs nowhere in `big`, `NULL` is returned;
otherwise a pointer to the first character of
the first occurrence of `little` is returned. */
char	*ft_strnstr(const char *big, const char *little, size_t len);

/* Converts the initial portion of string `str`,
returning it as an int.
@param str String to convert.
@return Integer representation of `str`. */
int		ft_atoi(const char *str);

/* Allocates memory for an array
of `nmemb` elements of `size` bytes each
and returns a pointer to the allocated memory.
The memory is set to zero.  If `nmemb` or `size` is `0`,
then `calloc()` returns a unique pointer value
that can later be successfully passed to `free()`.
@param nmemb Number of elements in the array.
@param size Size of each element in the array.
@return Pointer to the allocated memory. */
void	*ft_calloc(size_t nmemb, size_t size);

/* Returns a pointer to a new string,
which is a duplicate of the string `s`.
Memory for the new string is obtained with `malloc(3)`.
@param src String to duplicate.
@return Pointer to a new string which is a duplicate of `src`.
It returns `NULL` if insufficient memory was available. */
char	*ft_strdup(const char *src);

/*
PART 2
*/

/* Allocates memory using `malloc(3)` and returns
a substring from the string `s`.
The substring starts at index `start` and has
a maximum length of `len`.
The NUL-terminator is included in `len`.
@param s Original string from which to create the substring.
@param start Starting index of the substring within `s`.
@param len Maximum length of the substring.
@return Pointer to a new substring.
`NULL` if the allocation fails. */
char	*ft_substr(const char *s, unsigned int start, size_t len);

/* Allocates memory using `malloc(3)` and returns a
new string, which is the result of concatenating `s1` and `s2`.
@param s1 Prefix string.
@param s2 Suffix string.
@return Pointer to a new, joined string.
`NULL` if the allocation fails. */
char	*ft_strjoin(const char *s1, const char *s2);

/* Allocates memory using `malloc(3)` and returns
a copy of `s1` with characters from `set` removed
from the beginning and the end.
@param s1 String to be trimmed.
@param set String containing the set of characters to be removed.
@return Pointer to a new, trimmed string.
`NULL` if the allocation fails. */
char	*ft_strtrim(const char *s, const char *set);

/* Allocates memory using `malloc(3)` and returns
an array of strings obtained by splitting `s` using
the character `c` as a delimiter.
The array ends with a `NULL` pointer.
@param s String to be split.
@param c Delimiter character.
@return Array of new strings resulting from the split.
`NULL` if the allocation fails. */
char	**ft_split(char const *s, char c);

/* Allocates memory using `malloc(3)` and returns
a string representing `n`.
@param n Integer to convert.
@return String representing `n`.
`NULL` if the allocation fails. */
char	*ft_itoa(int n);

/* Applies the function `f` to each character of
the string `s`, passing its index as the first argument
and the character itself as the second.
A new string is created using `malloc(3)` to store
the results from the successive applications of `f`.
@param s String to iterate over.
@param f Function to apply to each character.
@return String created from the successive applications of `f`.
`NULL` if the allocation fails. */
char	*ft_strmapi(char const *s, char (*f)(unsigned int, char));

/* Applies the function `f` to each character of
the string passed as argument, passing its index as
the first argument. Each character is passed by
address to `f` so it can be modified if necessary.
@param s String to iterate over.
@param f Function to apply to each character. */
void	ft_striteri(char *s, void (*f)(unsigned int, char*));

/* Outputs the character `c` to
the specified file descriptor.
@param c Character to output.
@param fd File descriptor on which to write. */
void	ft_putchar_fd(char c, int fd);

/* Outputs the string `s` to
the specified file descriptor.
@param s String to output.
@param fd File descriptor on which to write. */
void	ft_putstr_fd(char *s, int fd);

/* Outputs the string `s` to
the specified file descriptor,
followed by a newline.
@param s String to output.
@param fd File descriptor on which to write. */
void	ft_putendl_fd(char *s, int fd);

/* Outputs the integer `n` to
the specified file descriptor.
@param n Integer to output.
@param fd File descriptor on which to write. */
void	ft_putnbr_fd(int n, int fd);

/*
BONUS PART
*/

/* Allocates memory using `malloc(3)` and returns
a new node. The `content` member variable is
initialized with the given parameter `content`.
The variable `next` is initialized to `NULL`.
@param content Content to store in the new node.
@return Pointer to the new node. */
t_list	*ft_lstnew(void *content);

/* Adds the node `new` at the beginning of a list.
@param lst Address of a pointer to the first node of a list.
@param new Pointer to the node to be added. */
void	ft_lstadd_front(t_list **lst, t_list *new);

/* Counts the number of nodes in a list.
@param lst Beginning of the list.
@return Length of the list. */
int		ft_lstsize(t_list *lst);

/* Finds the last node of a list.
@param lst Beginning of the list.
@return Last node of the list. */
t_list	*ft_lstlast(t_list *lst);

/* Adds the node `new` at the end of a list.
@param lst Address of a pointer to a node.
@param new Pointer to the node to be added. */
void	ft_lstadd_back(t_list **lst, t_list *new);

/* Frees the content of a node using the function `del`.
Then, frees the node itself. Does NOT free the next node.
@param lst Node to free.
@param del Address of the function used to delete the content. */
void	ft_lstdelone(t_list *lst, void (*del)(void*));

/* Deletes and frees the given node and all its
successors, using the function `del` and `free(3)`.
Finally, set the pointer to the list to `NULL`.
@param lst Address of a pointer to a node.
@param del Address of the function used to delete
the content of the node. */
void	ft_lstclear(t_list **lst, void (*del)(void*));

/* Iterates through the list `lst` and applies the
function `f` to the content of each node.
@param lst Address of a pointer to a node.
@param f Address of the function to apply to each node’s content. */
void	ft_lstiter(t_list *lst, void (*f)(void *));

/* Iterates through the list `lst`, applies the
function `f` to each node’s content, and creates
a new list resulting of the successive applications
of the function `f`. The `del` function is used to
delete the content of a node if needed.
@param lst Address of a pointer to a node.
@param f Address of the function applied to each node’s content.
@param del Address of the function used to delete a
node’s content if needed.
@return New list. `NULL` if the allocation fails. */
t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *));

#endif
