with open("7.input", "r") as f:
    content = f.readlines()

graph = []
for line in content:
    graph.append([])
    for c in line.strip():
        if c == "S":
            graph[-1].append([1])
        elif c == ".":
            graph[-1].append([0])
        elif c == "^":
            graph[-1].append([-1])
        else:
            raise NotImplementedError

barrier = -1
for line_idx in range(1, len(graph[1:])+1):
    for elem_idx in range(len(graph[line_idx])):
        upper_flow = graph[line_idx-1][elem_idx][0]
        curr_terrain = graph[line_idx][elem_idx][0]
        # Flow to barrier
        if curr_terrain == barrier:
            if elem_idx == 0:
                graph[line_idx][elem_idx+1][0] += upper_flow
            elif elem_idx == len(graph[line_idx]) - 1:
                graph[line_idx][elem_idx-1][0] += upper_flow
            else:
                graph[line_idx][elem_idx-1][0] += upper_flow
                graph[line_idx][elem_idx+1][0] += upper_flow
        # Flow naturally
        elif curr_terrain != barrier and upper_flow != barrier:
            graph[line_idx][elem_idx][0] += upper_flow

result = 0
for lst in graph[-1]:
    curr_result = lst[0]
    result += curr_result if curr_result > barrier else 0
print(result)