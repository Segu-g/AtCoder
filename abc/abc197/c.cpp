#include <iostream>
#include <algorithm>


using ull = uint64_t;

ull calc(int n, ull a[], ull bit){
    ull ret = 0;
    ull val = 0;
    for(int i = 0; i < n - 1; i++){
        val |= a[i];
        if (bit % 2){
            // std::cout << "    " << bit << " : " << val << std::endl;
            ret ^= val;
            val = 0;
        }
        bit = bit >> 1;
    }
    val |= a[n-1];
    // std::cout << "    " << bit << " : " << val << std::endl;
    ret ^= val;
    return ret;
}


int main(){
    int n;
    std::cin >> n;
    ull a[20];
    for(int i = 0; i < n; i++){
        std::cin >> a[i];
    }
    ull loop = 1 << (n - 1);
    ull min_val = calc(n, a, 0);
    // std::cout << 0 << " : " << min_val << std::endl;
    for(ull bit = 1; bit < loop; bit++){
        ull ret = calc(n, a, bit);
        // std::cout << bit << " : " << ret << std::endl;
        min_val = std::min(min_val, ret);
    }
    std::cout << min_val << std::endl;
}
