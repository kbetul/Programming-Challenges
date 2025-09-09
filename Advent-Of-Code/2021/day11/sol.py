data = """
1564524226
1384554685
7582264835
8812672272
1161463137
7831762344
2855527748
6141737874
8611458313
8215372443
"""
# Turn into 2D list of integers
grid = [[int(c) for c in line] for line in data.strip().splitlines()]

total_flashes = 0
for _ in range(100):  # simulate 100 steps
    flashed = set()
    # Step 1: increase all by 1
    for r in range(10):
        for c in range(10):
            grid[r][c] += 1
    # Step 2: flash while possible
    while True:
        new_flash = False
        for r in range(10):
            for c in range(10):
                if grid[r][c] > 9 and (r, c) not in flashed:
                    flashed.add((r, c))
                    new_flash = True
                    # increase neighbors
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < 10 and 0 <= nc < 10:
                                grid[nr][nc] += 1
        if not new_flash:
            break
    # Step 3: reset flashed to 0
    for r, c in flashed:
        grid[r][c] = 0
    #For Part 2 (the “sync step”), you can detect if 
    #len(flashed) == R*C and return that step index.
    total_flashes += len(flashed)
print(total_flashes)  # 1656 for the example
