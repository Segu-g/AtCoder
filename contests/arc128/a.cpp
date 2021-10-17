#include <iostream>
#include <vector>

int main()
{
    uint64_t n;
    std::cin >> n;
    uint64_t *a_array = new uint64_t[n];

    for (size_t i = 0; i < n; i++)
    {
        std::cin >> a_array[i];
    }

    double *max_vals = new double[(n + 1) * 2];
    bool *flags = new bool[n * 2];
    max_vals[0] = 1;
    max_vals[1] = 0;

    for (size_t i = 0; i < n; i++)
    {
        uint64_t a = a_array[i];
        double gold = max_vals[2 * i];
        double silver = max_vals[2 * i + 1];

        double next_gold;
        bool op_gold;
        if (a * gold > silver)
        {
            next_gold = silver / a;
            op_gold = true;
        }
        else
        {
            next_gold = gold;
            op_gold = false;
        }
        max_vals[(i + 1) * 2] = next_gold;
        flags[i * 2] = op_gold;

        double next_silver;
        bool op_silver;
        if (a * gold < silver)
        {
            next_silver = gold * a;
            op_silver = true;
        }
        else
        {
            next_silver = silver;
            op_silver = false;
        }
        max_vals[(i + 1) * 2 + 1] = next_silver;
        flags[i * 2 + 1] = op_silver;
    }

    bool *ops = new bool[n];
    bool silver_flag = false;
    for (size_t i = n - 1; i >= 0; i--)
    {
        ops[i] = flags[2 * i + silver_flag];
        silver_flag = ops[i] ^ silver_flag;
    }

    bool is_first = true;
    for (size_t i = 0; i < n; i++)
    {
        if (!is_first)
        {
            std::cout << " ";
        }
        std::cout << ops[i];
    }

    is_first = true;
    for (size_t i = 0; i < n + 1; i++)
    {
        if (!is_first)
        {
            std::cout << " ";
        }
        std::cout << max_vals[2 * i];
    }

    is_first = true;
    for (size_t i = 0; i < n; i++)
    {
        if (!is_first)
        {
            std::cout << " ";
        }
        std::cout << max_vals[2 * i + 1];
    }

    is_first = true;
    for (size_t i = 0; i < n + 1; i++)
    {
        if (!is_first)
        {
            std::cout << " ";
        }
        std::cout << flags[2 * i];
    }

    is_first = true;
    for (size_t i = 0; i < n + 1; i++)
    {
        if (!is_first)
        {
            std::cout << " ";
        }
        std::cout << flags[2 * i];
    }
}