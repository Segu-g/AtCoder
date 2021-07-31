s1 = input()
s2 = input()
s3 = input()
char_set = set(s1) | set(s2) | set(s3)
char_lst = list(char_set)
top_char_set = set((s1[0], s2[0], s3[0]))

def build_val(char_map, masked_num):
    num = 0
    dig = 1
    for c in masked_num[::-1]:
        num += char_map[c] * dig
        dig *= 10
    return num


def search(char_map, char_lst, num_set):
    # print(char_map, char_lst, num_set)
    if len(char_lst) == 0:
        s1_num = build_val(char_map, s1)
        s2_num = build_val(char_map, s2)
        s3_num = build_val(char_map, s3)
        ret = s1_num + s2_num == s3_num
        if ret:
            print(s1_num)
            print(s2_num)
            print(s3_num)
        return ret
    else:
        ret = False
        for n in num_set:
            if n == 0 and char_lst[-1] in top_char_set:
                continue
            char_map[char_lst[-1]] = n
            if search(char_map, char_lst[:-1], num_set - {n}):
                return True
        return False


if len(char_lst) > 10 or not search(dict(), char_lst, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}):
    print("UNSOLVABLE")
