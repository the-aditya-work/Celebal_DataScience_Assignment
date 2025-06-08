
def lower_triangular(n):
    print("\nLower Triangular Pattern:")
    for i in range(1, n + 1):
        print("*" * i)

def upper_triangular(n):
    print("\nUpper Triangular Pattern:")
    for i in range(n):
        print(" " * i + "*" * (n - i))

def pyramid(n):
    print("\nPyramid Pattern:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)


try:
    rows = int(input("Enter the number of rows: "))
    if rows <= 0:
        print("Please enter a positive integer.")
    else:
        lower_triangular(rows)
        upper_triangular(rows)
        pyramid(rows)
except ValueError:
    print("Invalid input! Please enter an integer.")