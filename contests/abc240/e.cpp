#include <iostream>
#include <vector>

int create_ans(
    std::vector<std::pair<int, int>> &ans,
    std::vector<std::vector<int>> &edges,
    int target,
    int parent,
    int left);

int main()
{
    int n;
    std::cin >> n;

    std::vector<std::vector<int>> edges(n);

    for (int i = 0; i < n - 1; i++)
    {
        int u, v;
        std::cin >> u >> v;
        u -= 1;
        v -= 1;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }

    std::vector<std::pair<int, int>> ans(n);

    create_ans(
        ans,
        edges,
        0,
        -1,
        1);

    for (int i = 0; i < n; i++)
    {
        std::cout << ans[i].first << " " << ans[i].second << "\n";
    }
    std::cout << std::endl;
}

int create_ans(
    std::vector<std::pair<int, int>> &ans,
    std::vector<std::vector<int>> &edges,
    int target,
    int parent,
    int left)
{
    // std::cout << "target: " << target << ", left: " << left << std::endl;
    int width = 0;
    std::vector<int> &childs = edges[target];
    for (int i = 0; i < childs.size(); i++)
    {
        auto child = childs[i];
        if (child == parent)
        {
            continue;
        }
        width += create_ans(
            ans,
            edges,
            child,
            target,
            left + width);
    }
    width = width != 0 ? width : 1;
    ans[target].first = left;
    ans[target].second = left + width - 1;
    return width;
}