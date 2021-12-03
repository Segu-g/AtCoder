#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int64_t n, w;
    std::cin >> n >> w;
    std::vector<std::pair<int64_t, int64_t>> vec;
    for (int64_t i = 0; i < n; ++i)
    {
        int64_t a, b;
        std::cin >> a >> b;
        vec.push_back(std::make_pair(a, b));
    }
    std::sort(vec.begin(), vec.end(), std::greater<std::pair<int64_t, int64_t>>{});
    int64_t umami = 0;
    for (auto i = vec.begin(); i != vec.end() && w != 0; ++i)
    {
        int64_t weight = std::min(i->second, w);
        umami += weight * i->first;
        w -= weight;
    }
    std::cout << umami << std::endl;
    return 0;
}