import math

with open("8.input", "r") as f:
    content = f.readlines()

def calc_dist(x1, y1, z1, x2, y2, z2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2) + math.pow(z1 - z2, 2))

def get_visit_node_num(l):
    result = 0
    for i in l:
        if not node_visited[i]:
            result += 1
    return result

coordinate_list = []
distance_list = []

for line in content:
    coordinate_list.append([int(x) for x in line.strip().split(",")])

for i in range(len(coordinate_list)):
    for j in range(i + 1, len(coordinate_list)):
        distance = calc_dist(coordinate_list[i][0], coordinate_list[i][1], coordinate_list[i][2], coordinate_list[j][0], coordinate_list[j][1], coordinate_list[j][2])
        distance_list.append([[i, j], distance])

distance_list.sort(key=lambda x: x[1])

node_visited = [False for i in range(len(coordinate_list))]
node_num, connect_num = 0, 0
for distance_elem in distance_list:
    connect_from, connect_to = distance_elem[0]
    if not node_visited[connect_from] and not node_visited[connect_to]:
        node_visited[connect_from] = True
        node_visited[connect_to] = True
        node_num += 2
        connect_num += 1
    elif not node_visited[connect_from] and node_visited[connect_to]:
        node_visited[connect_from] = True
        node_num += 1
        connect_num += 1
    elif node_visited[connect_from] and not node_visited[connect_to]:
        node_visited[connect_to] = True
        node_num += 1
        connect_num += 1
    else:
        connect_num += 1
    
    if connect_num >= len(coordinate_list) - 1 and node_num == len(coordinate_list):
        print(coordinate_list[connect_from][0] * coordinate_list[connect_to][0])
        break