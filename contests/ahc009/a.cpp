#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <queue>

constexpr char DIRECTIONS[] = "UDLR";

char h[20][19];
char v[19][20];

int s_i, s_j, t_i, t_j;
double p;

using Pos = std::pair<int, int>;
using Node = std::pair<Pos, bool>;

class NodeHash
{
public:
    size_t operator()(const Node &x) const
    {
        return std::hash<int>()(x.first.first << 10) ^ std::hash<int>()(x.first.second << 20) ^ std::hash<bool>()(x.second);
    }
};

using UOS = std::unordered_set<Node, NodeHash>;
using Paths = std::unordered_map<Node, UOS, NodeHash>;
Paths paths;
std::unordered_set<Node, NodeHash> res_node;

bool check_wall(Pos pos, bool direc_i, bool up)
{
    if (up)
    {
        if (direc_i && pos.first == 19)
            return true;
        if (!direc_i && pos.second == 19)
            return true;
        if (direc_i)
        {
            return v[pos.first][pos.second] == '1';
        }
        else
        {
            return h[pos.first][pos.second] == '1';
        }
    }
    else
    {
        if (direc_i && pos.first == 0)
            return true;
        if (!direc_i && pos.second == 0)
            return true;
        if (direc_i)
        {
            return v[pos.first - 1][pos.second] == '1';
        }
        else
        {
            return h[pos.first][pos.second - 1] == '1';
        }
    }
}

bool move_pos(Pos &pos, bool direc_i, bool up)
{
    if (direc_i)
    {
        while (!check_wall(pos, direc_i, up))
        {
            pos.first += up ? 1 : -1;
        }
    }
    else
    {
        while (!check_wall(pos, direc_i, up))
        {
            pos.second += up ? 1 : -1;
        }
    }
}

void create_graph()
{
    std::queue<Node> queue;
    Pos start = std::make_pair(s_i, s_j);
    Pos start_u, start_d, start_l, start_r;
    start_u = start;
    start_d = start;
    start_l = start;
    start_r = start;
    move_pos(start_u, true, false);
    move_pos(start_d, true, true);
    move_pos(start_l, false, false);
    move_pos(start_r, false, true);
    std::cout << "start_u:" << start_u.first << ", " << start_u.second << std::endl;
    std::cout << "start_d:" << start_d.first << ", " << start_d.second << std::endl;
    std::cout << "start_l:" << start_l.first << ", " << start_l.second << std::endl;
    std::cout << "start_r:" << start_r.first << ", " << start_r.second << std::endl;
    queue.push(std::make_pair(start_u, false));
    queue.push(std::make_pair(start_d, false));
    queue.push(std::make_pair(start_l, true));
    queue.push(std::make_pair(start_r, true));
    while (!queue.empty())
    {
        Node node = queue.back();
        queue.pop();
        if (paths.find(node) != paths.end())
            continue;
        auto [pos, direc_i] = node;
        Pos low = pos,
            hi = pos;
        move_pos(low, direc_i, false);
        move_pos(hi, direc_i, true);
        Node low_node = std::make_pair(low, !direc_i);
        Node hi_node = std::make_pair(hi, !direc_i);
        std::unordered_set<Node, NodeHash> set = {low_node, hi_node};
        paths.insert({node, set});
        queue.push(low_node);
        queue.push(hi_node);
    }

    for (auto &&path : paths)
    {
        std::cout << "{" << path.first.first.first << ", " << path.first.first.second << "}: ";
        for (auto &&next : path.second)
        {
            std::cout << "{" << next.first.first << ", " << next.first.second << "}, ";
        }
        std::cout << std::endl;
    }
}

int main()
{
    std::cin >> s_i >> s_j >> t_i >> t_j >> p;

    for (int i = 0; i < 20; ++i)
    {
        for (int j = 0; j < 19; ++j)
        {
            std::cin >> h[i][j];
        }
    }
    for (int i = 0; i < 19; ++i)
    {
        for (int j = 0; j < 20; ++j)
        {
            std::cin >> v[i][j];
        }
    }
    create_graph();

    return 0;
}