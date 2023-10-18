def print_triangle(n):
    for i in range(1, n + 1):
        spaces = ""  * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    for i in range(1, n + 1):
        spaces = " "  * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    for i in range(1, n + 1):
        spaces = "  "  * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

n = 10
print_triangle(n)


