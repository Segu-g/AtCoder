#include <iostream>

using i64 = int64_t;

int main()
{
    constexpr i64 MOD = 998244353;
    int n, m, k;
    std::pair<int, int> *inputs;

    std::cin >> n >> m >> k;

    inputs = new std::pair<int, int>[m];
    for (int i = 0; i < m; i++)
    {
        std::cin >> inputs[i].first >> inputs[i].second;
        inputs[i].first--;
        inputs[i].second--;
    }

    i64 *cases = new i64[n];
    i64 *cases_buffer = new i64[n];
    for (int i = 0; i < n; i++)
    {
        cases[i] = 0;
    }

    cases[0] = 1;

    i64 sum_case = 1;

    for (int depth = 0; depth < k; depth++)
    {
        for (int i = 0; i < n; i++)
        {
            cases_buffer[i] = (sum_case - cases[i] + MOD) % MOD;
        }
        i64 new_sum_case = (sum_case * (n - 1)) % MOD;

        for (int j = 0; j < m; j++)
        {
            auto x = inputs[j];
            cases_buffer[x.first] += MOD - cases[x.second];
            cases_buffer[x.first] %= MOD;
            cases_buffer[x.second] += MOD - cases[x.first];
            cases_buffer[x.second] %= MOD;
            new_sum_case = (new_sum_case - cases[x.first] + MOD) % MOD;
            new_sum_case = (new_sum_case - cases[x.second] + MOD) % MOD;
        }

        sum_case = new_sum_case;
        i64 *tmp = cases;
        cases = cases_buffer;
        cases_buffer = tmp;
    }

    std::cout << cases[0] << std::endl;

    return 0;
}