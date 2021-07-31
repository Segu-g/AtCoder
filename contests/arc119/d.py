def main():
    h, w = map(int, input().split())
    canvas = [list(map(lambda c: c == "R", input())) for _ in range(h)]

    row_lst = [[] for _ in range(h)]
    col_lst = [[] for _ in range(w)]

    for i in range(h):
        for j in range(w):
            if canvas[i][j]:
                row_lst[i].append((i, j))
                col_lst[j].append((i, j))

    row_state = [None for _ in range(h)]
    col_state = [None for _ in range(w)]


if __name__ == "__main__":
    main()
