#include <iostream>
#include <string>

int main()
{
    std::string s;
    std::cin >> s;
    int num = std::stoi(s.substr(0, s.length() - 4));
    int d = std::stoi(s.substr(s.length() - 3, 1));
    std::cout << num + (d >= 5) << std::endl;
}