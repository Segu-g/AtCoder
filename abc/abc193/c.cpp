#include <iostream>
#include <unordered_set>

using ll = int64_t;

int main(){
    ll n;
    std::cin >> n;
    std::unordered_set<ll> s;
    ll count = n;
    for (long i = 2; i * i <= n; i++) {
        ll c = i * i;
        while (c <= n) {
            s.insert(c);
            c *= i;
        }
    }
    std::cout << n - s.size() << std::endl;
}
