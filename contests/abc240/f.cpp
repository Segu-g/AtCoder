#include <iostream>
#include <vector>

int main()
{
    int t;
    std::cin >> t;
    for (int i = 0; i < t; t++)
    {
        solve();
    }
    return 0;
}

void solve()
{
    int n, m;
    std::cin >> n >> m;
    std::vector<std::pair<int, int>> vec(n);
    for (int i = 0; i < n; i++)
    {
        std::cin >> vec[i].first >> vec[i].second;
    }
    int64_t cumsum = 0;
    std::vector<int64_t> cumsum_vec(n);
    for (int i = 0; i < n; i++)
    {
        cumsum += vec[i].first * vec[i].second;
        cumsum_vec[i] = cumsum;
    }

    std::vector<int> positive_to_genative;
    for (int i = 0; i < n - 1; i++)
    {
        if (cumsum_vec[i] > 0 && cumsum_vec[i + 1] < 0)
        {
            int64_t x = -vec[i + 1].first, y = vec[i + 1].second;
            int64_t cumsum = cumsum_vec[i];
            positive_to_genative.push_back(y + cumsum / x);
        }
    }
}