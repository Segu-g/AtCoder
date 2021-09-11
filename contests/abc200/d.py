MOD = 200
n = int(input())
a_array = list(map(int, input().split()))
mod_set = [set() for _ in range(200)]

ans = None
for i in range(n):
    a = a_array[i]
    mod_a = a % MOD
    update_set = [set() for _ in range(MOD)]
    update_set[mod_a].add((i,))
    for mod_i in range(MOD):
        for lst in mod_set[mod_i]:
            update_set[(mod_i + mod_a) % MOD].add((*lst, i))
    # breakpoint()
    for mod_i in range(MOD):
        mod_set[mod_i].update(update_set[mod_i])
    for mod_i in range(MOD):
        if len(mod_set[mod_i]) >= 2:
            # print(mod_set[mod_i])
            lst0 = mod_set[mod_i].pop()
            lst1 = mod_set[mod_i].pop()
            ans = (lst0, lst1)
            break
    if ans is not None:
        break

if ans is not None:
    print("Yes")
    print(len(ans[0]), " ".join(map(lambda x: str(x + 1), ans[0])))
    print(len(ans[1]), " ".join(map(lambda x: str(x + 1), ans[1])))
else:
    print("No")
