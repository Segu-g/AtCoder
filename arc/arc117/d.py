
n = int(input())
path = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    path[a].append(b)
    path[b].append(a)

def get_farthest_nodes(node, parent_node):
    if len(path[node]) == 1 and parent_node != None:
        return (0, [node])
    else:
        max_dist = 0
        farthest_nodes = []
        for child_node in path[node]:
            if child_node == parent_node:
                continue
            dist, ret_nodes = get_farthest_nodes(child_node, node)
            if dist > max_dist:
                max_dist = dist
                farthest_nodes = ret_nodes
            elif dist == max_dist:
                farthest_nodes.extend(ret_nodes)
        return (max_dist+1, farthest_nodes)

def calc_weight(lst):
    sum = 0
    for i, num in enumerate(lst):
        sum += (i+1) * num
    return sum


def build_dist_list(node, parent_node, depth, lst):
    lst[depth] += 1
    for child_node in path[node]:
        if child_node == parent_node:
            continue
        build_dist_list(child_node, node, depth+1, lst)

def build_best_tree(node, parent_node, val, lst):
    lst[node] = val
    for child_node in path[node]:
        if child_node == parent_node:
            continue
        build_best_tree(child_node, node, val+1, lst)


root = 0
if len(path[root]) == 1:
    dist, nodes = get_farthest_nodes(root, None)
    nodes.append(root)
else:
    ret = sorted(map(lambda node: get_farthest_nodes(node, root), path[root]),
        key=lambda x: x[0])[-2:]
    dist1, nodes1 = ret[1]
    dist2, nodes2 = ret[0]
    dist = dist1 + dist2 + 2
    nodes1.extend(nodes2)
    nodes = nodes1



# breakpoint()
best_root = nodes[0]
best_score = float("inf")
for node in nodes:
    dist_dist = [0 for _ in range(dist+1)]
    build_dist_list(node, None, 0, dist_dist)
    score = calc_weight(dist_dist)
    if score < best_score:
        best_score = score
        best_root = node

best_tree = [0 for _ in range(n)]
build_best_tree(best_root, None, 1, best_tree)
print(" ".join(map(str, best_tree)))
