with open("5.input", "r") as f:
    content = f.readlines()

range_list, num_list = [], []

num_mode = False
for line in content:
    if len(line.strip()) == 0:
        num_mode = True
        continue
    if num_mode:
        num_list.append(int(line.strip()))
    else:
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

num_list = sorted(num_list)
valid_count = 0
for num in num_list:
    for range_elem in sanitized_range_list:
        if range_elem[0] <= num <= range_elem[1]:
            valid_count += 1
            break

print(valid_count)
