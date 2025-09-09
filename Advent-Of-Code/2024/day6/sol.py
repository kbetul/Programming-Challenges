def read_file(pathname: str) -> list:
    result = []
    with open(pathname, 'r') as f:
        for line in f:
            result.append(list(line.strip()))
    return result

def solution(grid):
    rows, cols = len(grid), len(grid[0])

    # Direction mapping: (dx, dy)
    directions = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
    }

    # Right turns: how to rotate direction
    right_turn = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^',
    }

    # Find guard's starting position and direction
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in directions:
                x, y = i, j
                dir = grid[i][j]
                break

    visited = set()
    visited.add((x, y))

    while True:
        dx, dy = directions[dir]
        nx, ny = x + dx, y + dy

        # Exit if moving off the map
        if not (0 <= nx < rows and 0 <= ny < cols):
            break

        # If blocked, turn right and try again
        if grid[nx][ny] == '#':
            dir = right_turn[dir]
        else:
            # Move forward
            x, y = nx, ny
            visited.add((x, y))

    return len(visited)

def main():
    arr = read_file('input.txt')
    result = solution(arr)
    print(result)

if __name__ == "__main__":
    main()