#include <iostream>

int main()
{
    int64_t a, b;
    std::cin >> a >> b;
    bool easy = true;
    while (a != 0 && b != 0)
    {
        int64_t da = a % 10, db = b % 10;
        easy &= da + db < 10;
        a /= 10;
        b /= 10;
    }
    std::cout << (easy ? "Easy" : "Hard") << std::endl;
    return 0;
}