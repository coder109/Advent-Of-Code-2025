with open("3.input", "r") as f:
    content = f.readlines()

def find_max_in_line(line: str):
    max_val, max_idx = -1, -1
    for i in range(len(line)):
        if int(line[i]) > max_val:
            max_val = int(line[i])
            max_idx = i
    return max_val, max_idx

result = 0
for line in content:
    line = line.strip()
    temp_result = 0
    first_idx = 0
    for idx in range(12):
        first_large, tmp_first_idx = find_max_in_line(line[first_idx:-11 + idx if idx-11 != 0 else None])
        if first_large == -1:
            first_large = int(line[first_idx])
            tmp_first_idx = 0
        first_idx = first_idx + tmp_first_idx + 1
        temp_result = temp_result * 10 + first_large
    result += temp_result

print(result)