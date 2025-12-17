with open("4.input", "r") as f:
    content = f.readlines()

height, width = len(content), len(content[0].strip())

graph = [[0 for _ in range(width+2)] for _ in range(height+2)]

total_result = 0
result = 0


for h_idx in range(1, height+1):
    for w_idx in range(1, width+1):
        curr_item = content[h_idx-1][w_idx-1]
        if curr_item == "@":
            graph[h_idx][w_idx] = 1

while True:
    result = 0
    mem_list = []


    for h_idx in range(1, height+1):
        for w_idx in range(1, width+1):
            if graph[h_idx][w_idx] == 0:
                continue
            adjacent_num = 0
            if graph[h_idx-1][w_idx] == 1:
                adjacent_num += 1
            if graph[h_idx+1][w_idx] == 1:
                adjacent_num += 1
            if graph[h_idx][w_idx-1] == 1:
                adjacent_num += 1
            if graph[h_idx][w_idx+1] == 1:
                adjacent_num += 1
            if graph[h_idx+1][w_idx+1] == 1:
                adjacent_num += 1
            if graph[h_idx+1][w_idx-1] == 1:
                adjacent_num += 1
            if graph[h_idx-1][w_idx+1] == 1:
                adjacent_num += 1
            if graph[h_idx-1][w_idx-1] == 1:
                adjacent_num += 1
            if adjacent_num < 4:
                result += 1
                mem_list.append([h_idx, w_idx])
    if result == 0:
        break
    for mem in mem_list:
        graph[mem[0]][mem[1]] = 0
    total_result += result
        

print(total_result)