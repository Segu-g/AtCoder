#include <iostream>
#include <vector>
#include <algorithm>

using ll = int64_t;

constexpr ll MOD = 998244353;
constexpr ll MAX_DEPTH = 18;



constexpr ll power(ll a, ll b){
	ll res = 1;
	while(b > 0){
		if(b & 1) res = res * a % MOD;
		a = a * a % MOD;
		b >>= 1;
	}
	return res;
}

int main(){
    ll n, m;
    std::cin >> n >> m;
    m++;
    ll max_depth = std::min(n, MAX_DEPTH);
    std::vector<std::vector<ll>> dp(max_depth, std::vector<ll>(m, 0));

    std::vector<ll> factory(max_depth + 1);
    std::vector<ll> factory_inv(max_depth + 1);
    std::vector<ll> coefficients(max_depth, 0);
    factory[1] = 1;
    for(ll f = 2; f < max_depth + 1; f++){
        factory[f] = (factory[f-1] * f) % MOD;
        // std::cout << factory[f] << std::endl;
    }
    for(ll f = 1; f < max_depth + 1; f++){
        factory_inv[f] = power(factory[f], MOD-2);
        // std::cout << (factory_inv[f] * factory[f]) % MOD << std::endl;
    }
    coefficients[0] = 1;
    for(ll f = 1; f < max_depth; f++){
        coefficients[f] = factory_inv[f];
        for(ll g = f; 0 < g; g--){
            coefficients[f] *= (n - g) % MOD;
            coefficients[f] %= MOD;
        }
    }



    ll ans = 0;
    for(ll i = 1; i < m; i++){
        dp[0][i] = 1;
        for(ll depth = 0; depth < max_depth; depth++){
            ans += (dp[depth][i] * coefficients[depth]) % MOD;
            ans %= MOD;
        }
        for(ll depth = 1; depth < max_depth; depth++){
            ll root = dp[depth-1][i];
            for(ll j = 2; i * j < m; j++){
                dp[depth][i*j] += root;
                dp[depth][i*j] %= MOD;
            }
        }
    }
    std::cout << ans << std::endl;

}
