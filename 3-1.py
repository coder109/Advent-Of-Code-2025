with open("3-test.input", "r") as f:
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
    first_large, first_idx = find_max_in_line(line)
    if first_idx == len(line) - 1:
        second_large, second_idx = find_max_in_line(line[:first_idx])
        result += second_large * 10 + first_large
    else:
        second_large, second_idx = find_max_in_line(line[first_idx+1:])
        result += first_large * 10 + second_large

print(result)