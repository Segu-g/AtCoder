#include <iostream>
#include <vector>
#include <unordered_map>




int main(){
    long long i, n, x, m, buf, before;
    long long result;
    std::vector<long long> cumulative_sum;
    std::cin >> n >> x >> m;
    std::unordered_map<long long, long long> mp;
    cumulative_sum.push_back(0);
    buf = 0;
    for(i=1; i<=n; i++){
        before = mp[x];
        mp[x] = i;
        buf = (buf + x);
        cumulative_sum.push_back(buf);
        // std::cout << buf << '\n';
        if(before!=0){
            long long rest_len = n - i;
            long long roop_len = i - before;
            long long roop_sum = cumulative_sum[i] - cumulative_sum[before];
            long long roop_rest = cumulative_sum[before + (rest_len % roop_len)] - cumulative_sum[before];
            result = cumulative_sum[i];
            result += roop_sum * (rest_len / roop_len);
            result += roop_rest;
            break;
        }
        x = (x * x) % m;
    }
    if(i>n){
        // std::cout << "last element" << '\n';
        // std::cout << cumulative_sum.size() << '\n';
        result = cumulative_sum.back();
    }
    std::cout << result << '\n';
    return 0;

}
