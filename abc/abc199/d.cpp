#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>


int64_t pow(int x, int d){
    if(d != 1){
        int64_t ret = pow(x, d >> 1);
        if (d % 2 != 0){
            ret *= x;
        }
        return ret;
    }
    return x;
}

int64_t count(
    size_t pos,
    std::vector<std::pair<int, int>>& path_dim,
    std::vector<std::vector<int>>& paths,
    std::vector<int>& color_map)
{
    if(--pos == 0){
        return 1;
    }
    auto [dim, index] = path_dim[pos];
    if(dim == 0){
        return pow(3, pos+1);
    }
    std::vector<int> path = paths[index];
    bool flags[4] = {true, true, true, true};
    for(int node : path){
        flags[color_map[node]] = false;
    }
    int64_t ret = 0;
    for (int color = 1; color < 4; color++){
        if(flags[color]){
            color_map[index] = color;
            ret += count(
                pos,
                path_dim,
                paths,
                color_map);
        }
    }
    color_map[index] = 0;
    return ret;
}

int main(){
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> paths(n);
    for (int i = 0; i < m; i++){
        int a, b;
        std::cin >> a >> b;
        a--;
        b--;
        paths[a].push_back(b);
        paths[b].push_back(a);
    }

    std::vector<std::pair<int, int>> path_dim(n, {0,0});
    for (int i = 0; i < n; i++){
        size_t len = paths[i].size();
        path_dim[i] = std::make_pair(len, int(i));
    }

    std::sort(path_dim.begin(), path_dim.end());
    std::vector<int> color_map(n, 0);
    
    int64_t ret = count(path_dim.size(), path_dim, paths, color_map);
    std::cout << ret << std::endl;
}

