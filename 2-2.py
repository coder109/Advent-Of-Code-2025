with open("2.input", "r") as f:
    content = f.readlines()

def str_to_valid(num: str):
    if len(num) == 1:
        return True
    for cut_elem_len in range(1, len(num) // 2 + 1):
        pattern = num[:cut_elem_len]
        is_good = False
        for target_idx in range(cut_elem_len, len(num), cut_elem_len):
            if num[target_idx:target_idx + cut_elem_len] != pattern:
                is_good = True
        if not is_good:
            return False
    return True

for line in content:
    id_list = line.split(",")
    res = 0.
    for id_elem in id_list:
        from_id, to_id = id_elem.split("-")
        for i in range(int(from_id), int(to_id) + 1):
            if not str_to_valid(str(i)):
                print(f"invalid: {i}")
                res += i
    print(res)