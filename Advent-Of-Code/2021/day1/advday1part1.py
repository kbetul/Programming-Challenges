def advday1():
    left_values = []
    right_values = []
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.strip():
            left, right = line.split()
            left_values.append(int(left))
            right_values.append(int(right))
    
    ordered_left = sorted(left_values)
    ordered_right = sorted(right_values)

    distance_list = []

    for i in range(len(ordered_left)):
        distance = abs(ordered_left[i] - ordered_right[i])
        distance_list.append(distance)

    total_distance = sum(distance_list)
    print(f"Total distance: {total_distance}")
if __name__ == "__main__":
    advday1()
