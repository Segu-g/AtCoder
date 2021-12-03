#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int get_unionfind_root(std::vector<int> &unionfind, int vertex)
{
    int p = unionfind[vertex];
    return p < 0 ? vertex : get_unionfind_root(unionfind, p);
}

int main()
{
    int n, m;
    std::cin >> n >> m;
    std::vector<int> unionfind(n, -1);
    std::vector<std::pair<int, int>> edges;
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        std::cin >> a >> b;
        a--;
        b--;
        edges.push_back(std::make_pair(a, b));
    }
    std::sort(edges.begin(), edges.end());

    std::vector<int> ans_vec;
    ans_vec.push_back(0);

    for (int i = n - 1; i > 0; --i)
    {
        int net_count = ans_vec.back();
        net_count++;
        while (!edges.empty() && edges.back().first == i)
        {
            auto edge = edges.back();
            edges.pop_back();
            int i_root = get_unionfind_root(unionfind, i);
            int sec_root = get_unionfind_root(unionfind, edge.second);
            if (i_root != sec_root)
            {
                int i_root_count = -unionfind[i_root];
                int sec_root_count = -unionfind[sec_root];
                if (i_root_count < sec_root_count)
                {
                    std::swap(i_root, sec_root);
                    std::swap(i_root_count, sec_root_count);
                }
                unionfind[sec_root] = i_root;
                unionfind[i_root] = -(i_root_count + sec_root_count);
                net_count--;
                // std::cout
                //     << "stage:" << i
                //     << ", from:" << edge.second
                //     << ", root:" << root << std::endl;
            }
        }
        ans_vec.push_back(net_count);
    }
    for (auto ans = ans_vec.rbegin(); ans != ans_vec.rend(); ++ans)
    {
        std::cout << *ans << '\n';
    }
    std::cout << std::flush;
    return 0;
}