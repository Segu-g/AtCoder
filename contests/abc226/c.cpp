#include <iostream>
#include <vector>
#include <set>
#include <queue>

int main()
{
    size_t n;
    std::cin >> n;
    std::vector<int64_t> costs(n);
    std::vector<std::vector<size_t>> from(n);
    for (size_t i = 0; i < n; i++)
    {
        size_t k;
        std::cin >> costs[i] >> k;
        for (size_t j = 0; j < k; j++)
        {
            int64_t a;
            std::cin >> a;
            a -= 1;
            from[i].push_back(a);
        }
    }
    std::set<size_t> required_skill;
    std::set<size_t> buf_set(from[n - 1].begin(), from[n - 1].end());
    while (!buf_set.empty())
    {
        size_t ei = *buf_set.rbegin();
        if (required_skill.count(ei) == 0)
            required_skill.insert(ei);
        buf_set.erase(ei);
        for (const auto &from_i : from[ei])
        {
            if (buf_set.count(from_i) != 0)
            {
                buf_set.insert(from_i);
            }
        }
    }
    int64_t total_cost = costs[n - 1];
    for (const auto &ri : required_skill)
    {
        total_cost += costs[ri];
    }
    std::cout << total_cost << std::endl;
    return 0;
}