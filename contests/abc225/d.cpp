#include <iostream>

struct Train
{
    Train *before = nullptr;
    Train *after = nullptr;
    int value;
};

Train *trains;

void query1()
{
    int x, y;
    std::cin >> x >> y;
    x--;
    y--;
    trains[x].after = &trains[y];
    trains[y].before = &trains[x];
}

void query2()
{
    int x, y;
    std::cin >> x >> y;
    x--;
    y--;
    trains[x].after = nullptr;
    trains[y].before = nullptr;
}

void query3()
{
    int x;
    std::cin >> x;
    x--;
    Train *top = &trains[x];
    while (top->before != nullptr)
    {
        top = top->before;
    }
    int len = 1;
    Train *n = top;
    while (n->after != nullptr)
    {
        len++;
        n = n->after;
    }

    std::cout << len;
    for (Train *n = top; n != nullptr; n = n->after)
    {
        std::cout << " " << n->value;
    }
    std::cout << std::endl;
}

int main()
{
    int n, q;
    std::cin >> n >> q;
    trains = new Train[n];
    for (int i = 0; i < n; i++)
        trains[i].value = i + 1;

    for (int i = 0; i < q; i++)
    {
        int q;
        std::cin >> q;
        switch (q)
        {
        case 1:
            query1();
            break;

        case 2:
            query2();
            break;

        case 3:
            query3();
            break;
        }
    }
}