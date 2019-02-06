# This program displays a triangle pattern.
base_size = 8

for r in range(base_size):
    for c in range(r + 1):
        print('*', end='')
    print()
