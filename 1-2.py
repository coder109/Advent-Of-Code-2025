if __name__ == "__main__":
    with open("1.input", "r") as f:
        content = f.readlines()

    position = 50
    count = 0
    for line in content:
        position_to_zero_distance = position if line[0] == "L" else (100 - position)
        if position_to_zero_distance == 0:
            position_to_zero_distance = 100
        spin_distance = int(line[1:])
        if spin_distance >= position_to_zero_distance:
            count += (spin_distance - position_to_zero_distance) // 100 + 1
        if line[0] == "R":
            position += spin_distance
        elif line[0] == "L":
            position -= spin_distance

        position = position % 100

    print(count)