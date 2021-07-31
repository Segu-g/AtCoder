#include <iostream>

void print_mat(int h, int w, int* mat){
    for(int i=0; i<h; i++){
        for(int j=0; j<w; j++){
            std::cout << mat[i*w + j] << " ";
        }
        std::cout << std::endl;
    }
}


int main(){
    int h, w;
    std::cin >> h >> w;

    bool* map = new bool[h*w];
    int* dp = new int[h*w];
    
    for(int i=0; i<h*w; ++i){
        char c;
        std::cin >> c;
        map[i] = (c=='+');
    }
    if(map[h*w -1]){
        dp[h*w -1] = -1;
    }else {
        dp[h*w -1] = 1;
    }

    for(int sum=h+w-3; 0<=sum; --sum){
        for(int i=std::max(0, sum-w+1); i<std::min(h, sum+1); ++i){
            int j = sum - i;
            int index = w*i + j;
            int val;
            if(i==h-1){
                val = dp[index+1];
            }else if(j==w-1){
                val = dp[index+w];
            }else{
                val = std::min(dp[index+1], dp[index + w]);
            }
            if(map[index]){
                val = -1 - val;
            }else{
                val = 1 -val;
            }
            dp[index] = val;
        }
    }
    int res = dp[0];
    if(map[0]){
        res += 1;
    }else{
        res -= 1;
    }

    if(res > 0){
        std::cout << "Takahashi\n";
    }else if(res==0){
        std::cout << "Draw\n";
    }else{
        std::cout << "Aoki\n";
    }
    // print_mat(h, w, dp);
}


