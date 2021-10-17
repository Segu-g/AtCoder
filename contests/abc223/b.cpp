#include <iostream>
#include <string>

int main()
{
    std::string s;
    std::cin >> s;
    std::size_t len = s.length();
    std::string cat_str = s + s;
    std::string max_s = s;
    std::string min_s = s;
    for (size_t i = 0; i < len; i++)
    {
        std::string substr = cat_str.substr(i, len);
        if (substr > max_s)
            max_s = substr;
        if (substr < min_s)
            min_s = substr;
    }
    std::cout << min_s << std::endl;
    std::cout << max_s << std::endl;
    return 0;
}