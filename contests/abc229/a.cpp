#include <iostream>

int main()
{
    bool *grid = new bool[4];
    char c;
    for (int i = 0; i < 4; i++)
    {
        std::cin >> c;
        grid[i] = c == '#' ? true : false;
    }
    if (
        (grid[0] && grid[1]) || (grid[2] && grid[3]) || (grid[0] && grid[2]) || (grid[1] && grid[3]))
    {
        std::cout << "Yes" << std::endl;
    }
    else
    {
        std::cout << "No" << std::endl;
    }
    return 0;
}