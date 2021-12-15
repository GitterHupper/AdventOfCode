import numpy as np

with open('input.txt') as f:
    levels = np.array([list(map(int, line)) for line in f.read().splitlines()])
print(levels)
n = len(levels)

flashes = 0
steps = 0
while levels.any(): # Continue while any element is non-zero
    levels += 1
    flash = levels > 9
    flash_coords = list(zip(*np.where(flash)))
    flash_coords_new = flash_coords.copy()
    while flash.any():
        for fx, fy in flash_coords_new:
            for x,y in [(fx+i,fy+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
                if (x,y) not in flash_coords and x in range(n) and y in range(n):
                    levels[x][y] += 1
        levels[flash] = 0
        flash = levels > 9
        flash_coords_new = list(zip(*np.where(flash)))
        flash_coords += flash_coords_new

    if steps < 100:
        flashes += len(flash_coords)
    steps += 1

# Explicit answers
answer1 = flashes
answer2 = steps
print(f"flashes: {answer1}, steps: {answer2}")