#include <iostream>

int main(){
    constexpr int64_t MOD = 1000000007;

    int64_t n, p;
    std::cin >> n >> p;

    int64_t pm = p-1;
    int64_t good_n = pm;
    int64_t bad_n = 0;
    int64_t sum_n = pm;

    for(int64_t i=1; i<n; i++){
        bad_n = ((bad_n * pm) + good_n) % MOD;
        sum_n = (sum_n * pm) % MOD;
        good_n = (sum_n - bad_n) % MOD;
    }
    std::cout << good_n << std::endl;
    return 0;
}
