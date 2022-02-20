#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int64_t n, d;
    std::cin >> n >> d;
    int64_t *left_arr = new int64_t[n];
    int64_t *right_arr = new int64_t[n];
    for (int64_t i = 0; i < n; i++)
    {
        std::cin >> left_arr[i] >> right_arr[i];
    }

    std::pair<int64_t, int64_t> *items = new std::pair<int64_t, int64_t>[2 * n];
    for (int64_t i = 0; i < n; i++)
    {
        items[2 * i] = std::make_pair(left_arr[i], -(i + 1));
        items[2 * i + 1] = std::make_pair(right_arr[i] + d - 1, i + 1);
    }
    std::sort(items, items + 2 * n);
    std::vector<int64_t> living_lines;
    std::vector<bool> breaked(n, false);
    int64_t count = 0;
    for (int64_t i = 0; i < 2 * n; i++)
    {
        // std::cout << "{" << item.first << ", " << item.second << "}\n";
        const auto &item = items[i];
        if (item.second < 0)
        {
            const int64_t line = -item.second - 1;
            living_lines.push_back(line);
            // std::cout << "pos: " << item.first << ", count: " << count << ", line: " << line << ", push" << std::endl;
        }
        else
        {
            const int64_t line = item.second - 1;
            if (!breaked[line])
            {
                for (auto l : living_lines)
                {
                    breaked[l] = true;
                }
                count++;
                living_lines.clear();
            }
            // std::cout << "pos: " << item.first << ", count: " << count << ", line: " << line << ", pop" << std::endl;
        }
    }
    std::cout << count << std::endl;
    return 0;
}