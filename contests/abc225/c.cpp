#include <iostream>

int main()
{
    int n, m;
    std::cin >> n >> m;
    int *b = new int[n * m];
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            std::cin >> b[m * i + j];
        }
    }

    int base = b[0];
    int bi = ((base + 6) / 7) - 1;
    int bj = (base + 6) % 7;

    if (bi < 0 || bj < 0 || bj + m >= 7)
    {
        std::cout << "No" << std::endl;
        return 0;
    }

    bool flag = true;

    for (int i = 0; (i < n) && flag; ++i)
    {
        for (int j = 0; (j < m) && flag; ++j)
        {
            if (b[i * m + j] != (bi + i) * 7 + bj + j + 1)
            {
                flag = false;
            }
        }
    }
    std::cout << (flag ? "Yes" : "No") << std::endl;
}