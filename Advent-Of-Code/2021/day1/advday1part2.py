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

    ocurrences = {}
    for i in range(len(right_values)):
        if right_values[i] not in ocurrences:
            ocurrences[right_values[i]] = 1
        else:
            ocurrences[right_values[i]] += 1
    
    distance_list = []
    for i in left_values:
        distance_list.append(i*ocurrences.get(i,0))

    total_distance = sum(distance_list)
    print(f"Total distance: {total_distance}")
if __name__ == "__main__":
    advday1()