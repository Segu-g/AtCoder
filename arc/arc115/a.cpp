#include <iostream>
#include <vector>


int main(){
    int n, m;
    std::cin >> n >> m;
    int even = 0;
    int odd = 0;
    char s[21];
    for(int i = 0; i < n; i++){
        std::cin >> s;
        int count = 0;
        for(int k = 0; k < m; k++){
            if (s[k] == '1'){
                count += 1;
            }
        }
        if(count % 2){
            odd += 1;
        }else {
            even += 1;
        }
    }
    std::cout << odd * even << std::endl;
}
