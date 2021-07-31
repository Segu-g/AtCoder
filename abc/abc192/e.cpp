#include <iostream>
#include <vector>
#include <array>
#include <queue>

int main() {
    int n, m, x, y;
    std::cin >> n >> m >> x >> y;
    x = x-1;
    y = y-1;
    std::vector<std::vector<int[3]>> path(n);

    for(int i = 0; i < m; ++i) {
        int a, b, t, k;
        std::cin >> a >> b >> t >> k;
        a = a-1;
        b = b-1;
        path[a].push_back({b, t, k});
        path[b].push_back({a, t, k});
    }

    std::vector<int> time_flag(n, -1);
    std::priority_queue<
        std::pair<int, int>,
        std::vector<std::pair<int, int>>,
        std::greater<std::pair<int, int>>> queue;
        queue.push(std::make_pair(0, x));

    while (!queue.empty()) {
        auto [time, town] = queue.top();
        queue.pop();
        if (time_flag[y] != -1 && time_flag[y] < time) {
            break;
        }
        for (const auto& [next, t, k] : path[town]) {
            int next_time = ((time - 1) / k + 1) * k + t;
            if (time_flag[next] == -1 || next_time < time_flag[next]) {
                time_flag[next] = next_time;
                queue.push(std::make_pair(next_time, next));
            }
        }
    }


    std::cout << time_flag[y] << std::endl;
    return 0;
}
