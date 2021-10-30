#include <iostream>

int main()
{
    char s[3];
    std::cin >> s;
    if (s[0] == s[1] && s[0] == s[2])
    {
        std::cout << 1 << std::endl;
    }
    else if (s[0] == s[1] || s[1] == s[2] || s[2] == s[0])
    {
        std::cout << 3 << std::endl;
    }
    else
    {
        std::cout << 6 << std::endl;
    }
    return 0;
}