with open("9-test.input", "r") as f:
    content = f.readlines()

def calc_area(x1, y1, x2, y2):
    return (x2 - x1 + 1) * (abs(y2 - y1) + 1)


coordinate_list = []
for line in content:
    coordinate_list.append([int(x) for x in line.strip().split(",")])