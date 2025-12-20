with open("6.input", "r") as f:
    content = f.readlines()

for content_idx in range(len(content)):
    content[content_idx] = content[content_idx][:-1]


def add_num_buffer(num_buffer: list[str], op: str) -> int:
    result = 0 if op == '+' else 1
    idx = 0
    while idx < len(num_buffer[0]):
        curr_result = ""
        for line in num_buffer:
            curr_result += "" if line[idx] == "" else line[idx]
        result = result + int(curr_result) if op == '+' else result * int(curr_result)
        idx += 1
    return result

num_lines = content[:-1]
max_line_len = max([len(line) for line in num_lines])
raw_op_line = content[-1].strip()
op_line = []
for op_char in raw_op_line:
    if op_char == '+':
        op_line.append('+')
    elif op_char == '*':
        op_line.append('*')

idx, op_idx = 0, 0
num_buffer = ["" for _ in range(len(num_lines))]
result = 0

while idx < max_line_len :
    is_all_space = True
    for line in num_lines:
        if line[idx] != ' ':
            is_all_space = False
            break

    if is_all_space:
        result += add_num_buffer(num_buffer, op_line[op_idx])
        num_buffer = ["" for _ in range(len(num_lines))]
        op_idx += 1
    else:
        for line_idx, line in enumerate(num_lines):
            num_buffer[line_idx] += line[idx]
    idx += 1
result += add_num_buffer(num_buffer, op_line[op_idx])
num_buffer = ["" for _ in range(len(num_lines))]
print(result)
