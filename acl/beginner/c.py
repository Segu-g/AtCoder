n, m = map(int, input().split())
nodes = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    a,b = a-1, b-1
    nodes[a].append(b)
    nodes[b].append(a)

nodes_flag = [False for _ in range(n)]
count = 0
for i in range(n):
    # print("{}:{}".format(i, nodes_flag))
    if nodes_flag[i] is not True:
        count += 1
        nodes_flag[i] = True
        nodes_list = nodes[i]
        while len(nodes_list):
            new_nodes_list =[]
            for node in nodes_list:
                if nodes_flag[node]:
                    continue
                nodes_flag[node] = True
                for next_node in nodes[node]:
                    new_nodes_list.append(next_node)
            nodes_list = new_nodes_list
print(count-1)
