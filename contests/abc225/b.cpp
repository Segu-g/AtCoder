#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    int *edge_count = new int[n];
    for (size_t i = 0; i < n; i++)
        edge_count[i] = 0;
    for (size_t i = 0; i < n - 1; ++i)
    {
        int a, b;
        std::cin >> a >> b;
        --a;
        --b;
        edge_count[a]++;
        edge_count[b]++;
    }

    bool flag = true;
    bool find_root = false;
    for (size_t i = 0; i < n; i++)
    {
        int count = edge_count[i];
        if (count != 1)
        {
            if (count != n - 1 || find_root)
            {
                flag = false;
            }
            find_root = true;
        }
    }

    if (flag)
    {
        std::cout << "Yes" << std::endl;
    }
    else
    {
        std::cout << "No" << std::endl;
    }
    return 0;
}