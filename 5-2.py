with open("5.input", "r") as f:
    content = f.readlines()

range_list, num_list = [], []

for line in content:
    if len(line.strip()) == 0:
        break
    range_start, range_end = [int(x) for x in line.strip().split("-")]
    range_list.append([range_start, range_end])

# Build Range Tree
range_list = sorted(range_list, key=lambda x: x[0])
sanitized_range_list = [range_list[0]]
# Remove Overlapping Range
for range_idx in range(1, len(range_list)):
    curr_elem = range_list[range_idx]
    curr_start, last_end = curr_elem[0], sanitized_range_list[-1][1]
    if curr_start > last_end:
        sanitized_range_list.append(curr_elem)
    elif curr_start == last_end:
        sanitized_range_list[-1][1] = curr_elem[1]
    else:
        sanitized_range_list[-1][1] = max(curr_elem[1], last_end)

valid_count = 0
for range_elem in sanitized_range_list:
    valid_count += range_elem[1] - range_elem[0] + 1

print(valid_count)
