#include <iostream>
#include <algorithm>
#include <vector>

int main()
{
    int n;
    std::cin >> n;
    std::vector<bool> vec(2 * n + 1, false);
    for (size_t i = 0; i != 2 * n + 1; i++)
    {
        if (vec[i])
            continue;
        std::cout << i + 1 << std::endl;
        int aoki;
        std::cin >> aoki;
        if (aoki == 0)
            break;
        vec[aoki - 1] = true;
    }
    return 0;
}