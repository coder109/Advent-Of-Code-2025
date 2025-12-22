import math

def calc_dist(x1, y1, z1, x2, y2, z2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2) + math.pow(z1 - z2, 2))

def bfs(graph: list[list[int]], start: int, visited: list[bool], visit_stack: list[int]) -> int:
    max_hop = 1
    node_queue = [start]

    while len(node_queue) > 0:
        curr_node = node_queue.pop(0)
        for neighbor in graph[curr_node]:
            if visited[neighbor]:
                continue
            visited[neighbor] = True
            visit_stack.append(neighbor)
            node_queue.append(neighbor)
            max_hop = max(max_hop, len(visit_stack))
    return max_hop

distance_list = []
connect_limit = 1000

with open("8.input", "r") as f:
    content = f.readlines()

coordinate_list = []
for line in content:
    coordinate_list.append([int(x) for x in line.strip().split(",")])

for i in range(len(coordinate_list)):
    for j in range(i + 1, len(coordinate_list)):
        distance = calc_dist(coordinate_list[i][0], coordinate_list[i][1], coordinate_list[i][2], coordinate_list[j][0], coordinate_list[j][1], coordinate_list[j][2])
        distance_list.append([[i, j], distance])

distance_list.sort(key=lambda x: x[1])


graph = [[] for i in range(len(coordinate_list))]

for i in range(connect_limit):
    connect_from, connect_to = distance_list[i][0]
    graph[connect_from].append(connect_to)
    graph[connect_to].append(connect_from)

visited = [False for i in range(len(coordinate_list))]
hop_list = []
for i in range(len(coordinate_list)):
    if visited[i]:
        continue
    visited[i] = True
    visit_stack = [i]
    max_hop, curr_hop = 1, 1
    hop_list.append(bfs(graph, i, visited, visit_stack) if graph[i] != [] else 1)

hop_list.sort()
result = 1
result = result * hop_list[-1] * hop_list[-2] * hop_list[-3]
print(result)