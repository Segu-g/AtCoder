#include <iostream>
#include <vector>
#include <queue>

int main()
{
    int n, m;
    std::cin >> n >> m;
    std::vector<int> *from = new std::vector<int>[n];
    std::vector<int> *to = new std::vector<int>[n];
    for (int i = 0; i < m; i++)
    {
        int a, b;
        std::cin >> a >> b;
        a -= 1;
        b -= 1;
        from[a].push_back(b);
        to[b].push_back(a);
    }
    std::vector<int> roots;
    int *to_size_array = new int[n];
    for (int i = 0; i < n; i++)
    {
        to_size_array[i] = to[i].size();
        if (to[i].size() == 0)
            roots.push_back(i);
    }
    std::priority_queue<int, std::vector<int>, std::greater<int>> roots_queue(roots.begin(), roots.end());

    std::vector<int> output;
    while (!roots_queue.empty())
    {
        int p = roots_queue.top();
        roots_queue.pop();
        output.push_back(p + 1);
        for (auto i = from[p].begin(); i != from[p].end(); i++)
        {
            to_size_array[*i] -= 1;
            if (to_size_array[*i] == 0)
                roots_queue.push(*i);
        }
    }
    if (output.size() != n)
    {
        std::cout << -1 << std::endl;
    }
    else
    {
        std::string space = "";
        for (auto i = output.begin(); i != output.end(); i++)
        {

            std::cout << space << *i;
            space = " ";
        }
        std::cout << std::endl;
    }
    return 0;
}