#include <iostream>
#include <numeric>
#include <cassert>

long long extend_gcd(long long a, long long b, long long &p, long long &q){
    if(b==0){
        p = 1;
        q = 0;
        return a;
    }
    long long d = extend_gcd(b, a%b, q, p);
    q -= a/b * p;
    return d;
}

long long cn_remainder(long long a_0, long long m_0){
    return (a_0 % m_0 + m_0) % m_0;
}

template <class... Args>
long long cn_remainder(long long a_0, long long m_0, long long a_1, long long m_1, Args... args){
    long long p, q;
    long long d = extend_gcd(m_0, m_1, p, q);
    assert((a_0 - a_1)%d == 0);
    long long m = m_0 * (m_1/d);
    long long a = a_0 + (a_1 - a_0) /d * m_0 * p;
    a %= m;
    return cn_remainder(a, m, args...);
}



int main(void){
    long long a_0, a_1, m_0, m_1;
    std::cout << "a_0:";
    std::cin >> a_0;
    std::cout << "m_0:";
    std::cin >> m_0;
    std::cout << "a_1:";
    std::cin >> a_1;
    std::cout << "m_1:";
    std::cin >> m_1;
    std::cout << "cn_remainder(" << a_0 << "," << m_0 << "," << a_1 << "," << m_1 << ") is " << cn_remainder(a_0, m_0, a_1, m_1) << "\n";
    return 0;
}
