#include <iostream>
#include <vector>
#include <set>
#include <functional>

struct Less
{
    bool operator()(const std::vector<int> &vec_a, const std::vector<int> &vec_b) const
    {
        if (vec_a.size() != vec_b.size())
            return vec_a.size() < vec_b.size();

        std::size_t len = vec_a.size();
        for (std::size_t i = 0; i < len; ++i)
        {
            if (vec_a[i] != vec_b[i])
                return vec_a[i] < vec_b[i];
        }
        return false;
    };
};

int main()
{
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> vec(n);
    int sum_len = 0;
    for (int i = 0; i < n; i++)
    {
        int len;
        std::cin >> len;
        for (int k = 0; k < len; k++)
        {
            int a;
            std::cin >> a;
            vec[i].push_back(a);
        }
    }
    std::set<std::vector<int>, Less> vec_set;
    for (int i = 0; i < n; i++)
    {
        std::vector<int> e = vec[i];
        if (vec_set.count(e) == 0)
            vec_set.insert(e);
    }
    std::cout << vec_set.size() << std::endl;
}