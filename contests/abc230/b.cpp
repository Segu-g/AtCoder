#include <iostream>
#include <string>

int main()
{
    std::string s;
    std::cin >> s;
    for (int i = 0; i < 3; i++)
    {
        bool flag = true;
        for (int j = 0; j < s.length(); j++)
        {
            char c = (i + j) % 3 ? 'x' : 'o';
            if (c != s.at(j))
            {
                flag = false;
                break;
            }
        }
        if (flag)
        {
            std::cout << "Yes" << std::endl;
            return 0;
        }
    }
    std::cout << "No" << std::endl;
}