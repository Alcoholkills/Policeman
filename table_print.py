def table_print(list_one: list, list_two: list) -> None:
    if diff := len(list_one) - len(list_two) > 0:
        list_two += [""] * diff
    elif diff:= len(list_one) - len(list_two) < 0:
        list_one += [""] * diff
    final_list = list(zip(list_one, list_two))
    max_len = max_item_len(list_one)
    for tupp in final_list:
        print(f"{tupp[0]:>{max_len}}\t{tupp[1]}")

def max_item_len(l: list) -> int:
    max_len: int = len(str(l[0]))
    for item in l[1:]:
        if temp := len(str(item)) > max_len:
            max_len = temp
    return max_len


if __name__ == "__main__":
    l = ["OUIERIEROZEZAE", "doaz", "eazda"]
    m = [1, 2, 3, 4]
    table_print(l,m)
