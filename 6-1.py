with open("6.input", "r") as f:
    content = f.readlines()

operate_list, num_list_list = [], []
for line in content:
    line_elem = line.strip().split(" ")
    remove_list = []
    for idx in range(len(line_elem)):
        if len(line_elem[idx].strip()) == 0:
            remove_list.append(idx)

    for idx in sorted(remove_list, reverse=True):
        del line_elem[idx]
    if "*" in line_elem:
        operate_list = line_elem
    else:
        num_list_list.append(line_elem)

result = 0
for idx, operation in enumerate(operate_list):
    temp_result = 0
    if operation == "*":
        temp_result = 1
        for num_list in num_list_list:
            temp_result *= int(num_list[idx])
    elif operation == "+":
        for num_list in num_list_list:
            temp_result += int(num_list[idx])
    else:
        print(operation)
        raise NotImplementedError
    result += temp_result

print(result)