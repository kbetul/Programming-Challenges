'''
There is a rectangle of given width w and height h,

On the width side, you are given a list of measurements.
On the height side, you are given another list of measurements.

Draw perpendicular lines from the measurements to partition the rectangle into smaller rectangles.

In all sub-rectangles (include the combinations of smaller rectangles), how many of them are squares?


Example

w = 10
h = 5
measurements on x-axis: 2, 5
measurements on y-axis: 3

   ___2______5__________ 
  |   |      |          |
  |   |      |          |
 3|___|______|__________|
  |   |      |          |
  |___|______|__________|

Number of squares in sub-rectangles = 4 (one 2x2, one 3x3, two 5x5)
'''

from collections import Counter

def partition(w, h, x_measurements, y_measurements):
     # Step 1: Get full cut positions
    x_positions = [0]
    for i in x_measurements:
        x_positions.append(i)
    x_positions.append(w)
    y_positions = [0]
    for i in y_measurements:
        y_positions.append(i)
    y_positions.append(h)

    # Step 2: Get all possible segment lengths
    x_segments = []
    for i in range(len(x_positions)):
        for j in range(i + 1, len(x_positions)):
            x_segments.append(x_positions[j] - x_positions[i])

    y_segments = []
    for i in range(len(y_positions)):
        for j in range(i + 1, len(y_positions)):
            y_segments.append(y_positions[j] - y_positions[i])
    
    # Step 3: Count frequency of each segment length
    count_x = Counter(x_segments)
    count_y = Counter(y_segments)

    # Step 4: Count matching square sizes
    total_squares = 0
    for size in count_x:
        if size in count_y:
            total_squares += count_x[size] * count_y[size]
    
    return total_squares


def main():
    # Read input
    w, h, countX, countY = map(int, input().split())
    x_measurements = list(map(int, input().split()))
    y_measurements = list(map(int, input().split()))

    # Compute result
    result = partition(w, h, x_measurements, y_measurements)
    print(result)

if __name__ == "__main__":
    main()

