with open("7.input", "r") as f:
    content = f.readlines()

graph = []
for line in content:
    graph.append([])
    for c in line.strip():
        graph[-1].append(c if c != "S" else "1")

result = 0

for line_idx in range(len(graph[1:])):
    for char_idx in range(len(graph[line_idx])):
        if graph[line_idx-1][char_idx] == "1" and graph[line_idx][char_idx] == "^":
            result += 1
            if char_idx == 0 :
                graph[line_idx][char_idx+1] = "1"
            elif char_idx == len(graph[line_idx]) - 1:
                graph[line_idx][char_idx-1] = "1"
            else:
                graph[line_idx][char_idx-1] = "1"
                graph[line_idx][char_idx+1] = "1"
        elif graph[line_idx-1][char_idx] == "1":
            graph[line_idx][char_idx] = "1"

print(result)