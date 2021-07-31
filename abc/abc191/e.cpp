#include <iostream>
#include <vector>

class UnionFind{
public:
    int 
};

int main(){
    int n, m;
    std::cin >> n >> m;
    std::vector< std::map<int, int> > path(n);
    for(int i = 0; i < m; i++){
        int a, b, c;
        std::cin >> a >> b >> c;
        a--;
        b--;
        if (path[a].contains(b)){
            path[a].insert(std::make_pair(b, std::min(c, path[a].at(b))));
        }else{
            path[a].insert(std::make_pair(b, c));
        }
    }

}
