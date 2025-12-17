with open("2.input", "r") as f:
    content = f.readlines()

def str_to_valid(num: str):
    digit_num = len(num)
    if digit_num % 2 == 1:
        return True
    division = 10 ** (digit_num / 2) + 1
    return int(num) % division != 0

for line in content:
    id_list = line.split(",")
    res = 0.
    for id_elem in id_list:
        from_id, to_id = id_elem.split("-")
        for i in range(int(from_id), int(to_id) + 1):
            if not str_to_valid(str(i)):
                res += i
    print(res)