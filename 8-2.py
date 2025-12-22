with open("8-test.input", "r") as f:
    content = f.readlines()

coordinate_list = []
for line in content:
    coordinate_list.append([int(x) for x in line.strip().split(",")])