#include <iostream>

int main()
{
    int64_t n, a, b;
    std::cin >> n >> a >> b;
    int64_t p, q, r, s;
    std::cin >> p >> q >> r >> s;
    for (int64_t i = p; i <= q; i++)
    {
        for (int64_t j = r; j <= s; j++)
        {
            char color =
                (i - a == j - b) || (i - a == b - j) ? '#' : '.';
            std::cout << color;
        }
        std::cout << std::endl;
    }
}