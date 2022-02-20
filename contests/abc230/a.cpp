#include <iostream>
#include <iomanip>

int main()
{
    int n;
    std::cin >> n;
    if (n >= 42)
        n++;
    std::cout << "AGC" << std::setw(3) << std::setfill('0') << n << std::endl;
}