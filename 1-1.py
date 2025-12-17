with open("1.input", "r") as f:
    content = f.readlines()

initial_position = 50
count = 0
for line in content:
    if line[0] == "R":
        initial_position += int(line[1:])
    elif line[0] == "L":
        initial_position -= int(line[1:])
    initial_position = initial_position % 100
    if initial_position == 0:
        count += 1

print(count)