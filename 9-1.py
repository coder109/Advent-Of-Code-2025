with open("9.input", "r") as f:
    content = f.readlines()

def calc_area(x1, y1, x2, y2):
    return (x2 - x1 + 1) * (y2 - y1 + 1)


coordinate_list = []
for line in content:
    coordinate_list.append([int(x) for x in line.strip().split(",")])

max_area = 0
for i in range(len(coordinate_list)):
    for j in range(i + 1, len(coordinate_list)):
        x1, y1 = coordinate_list[i][0], coordinate_list[i][1]
        x2, y2 = coordinate_list[j][0], coordinate_list[j][1]
        max_area = max(max_area, calc_area(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))

print(max_area)