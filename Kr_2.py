n = int(input())

# Print the first half of the triangle
for i in range(1, n+1):
    print(*range(1, i+1), *range(i-1, 0, -1), sep='', end='\n')

# Print the second half of the triangle
for i in range(n-1, 0, -1):
    print(*range(1, i+1), *range(i-1, 0, -1), sep='', end='\n')