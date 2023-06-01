def print_triangle(n):
    if n > 0:
        print_triangle(n-1)
        print(str(n) * n)

height = int(input())

print_triangle(height)