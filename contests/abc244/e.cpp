#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
constexpr int64_t MOD = 998244353;

int main()
{
    int n, m, k, s, t, x;
    std::cin >> n >> m >> k >> s >> t >> x;
    s--;
    t--;
    x--;
    vector<vector<int>> paths(n);
    for (size_t i = 0; i < m; i++)
    {
        int u, v;
        std::cin >> u >> v;
        u--;
        v--;
        paths[u].push_back(v);
        paths[v].push_back(u);
    }

    vector<uint64_t> even_num(n, 0);
    vector<uint64_t> odd_num(n, 0);
    vector<uint64_t> prev_even_num(n);
    vector<uint64_t> prev_odd_num(n);
    even_num[s] = 1;
    for (size_t step = 0; step < k; step++)
    {
        std::copy(even_num.cbegin(), even_num.cend(), prev_even_num.begin());
        std::copy(odd_num.cbegin(), odd_num.cend(), prev_odd_num.begin());

        std::fill(even_num.begin(), even_num.end(), 0);
        std::fill(odd_num.begin(), odd_num.end(), 0);
        for (int v = 0; v < n; v++)
        {
            const int prev_even_pattern = prev_even_num[v];
            const int prev_odd_pattern = prev_odd_num[v];
            for (const int next : paths[v])
            {
                if (next == x)
                {
                    even_num[next] = (even_num[next] + prev_odd_pattern) % MOD;
                    odd_num[next] = (odd_num[next] + prev_even_pattern) % MOD;
                }
                else
                {
                    even_num[next] = (even_num[next] + prev_even_pattern) % MOD;
                    odd_num[next] = (odd_num[next] + prev_odd_pattern) % MOD;
                }
            }
        }
        // std::cout << "step: " << step << std::endl;

        // for (int i = 0; i < n; i++)
        // {
        //     std::cout << even_num[i] << " ";
        // }
        // std::cout << std::endl;
        // for (int i = 0; i < n; i++)
        // {
        //     std::cout << odd_num[i] << " ";
        // }
        // std::cout << std::endl;
    }
    std::cout << even_num[t] << std::endl;
    return 0;
}