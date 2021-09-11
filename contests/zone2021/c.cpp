#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

#include <algorithm>
#include <set>
#include <iterator>
#include <cstdio>


constexpr int STATUS_NUM = 5;

struct Element{
    int val;
    int index;
    bool operator<(const Element& right) const noexcept {
        return this->val > right.val;
    }
};


int main(){
    int n;
    scanf("%d", &n);

    Element** status_arrays = new Element*[STATUS_NUM];
    std::set<int> val_set;
    for(int status_i=0; status_i<STATUS_NUM; ++status_i){
        status_arrays[status_i] = new Element[n];
    }
    
    for(int i=0; i<n; ++i){
        int a, b, c, d, e;
        scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
        val_set.insert(a);
        val_set.insert(b);
        val_set.insert(c);
        val_set.insert(d);
        val_set.insert(e);
        status_arrays[0][i].val = a;
        status_arrays[0][i].index = i;
        status_arrays[1][i].val = b;
        status_arrays[1][i].index = i;
        status_arrays[2][i].val = c;
        status_arrays[2][i].index = i;
        status_arrays[3][i].val = d;
        status_arrays[3][i].index = i;
        status_arrays[4][i].val = e;
        status_arrays[4][i].index = i;
    }


    for(int status_i=0; status_i<STATUS_NUM; ++status_i){
        std::sort(
            status_arrays[status_i], 
            status_arrays[status_i] + n);
    }

    int* status_flags = new int[n];
    for(int i=0; i<n; ++i){
        status_flags[i] = 0;
    }
    int next_indexs[STATUS_NUM] = {0};
    bool flag = false;
    std::set<int> satisfied_set;
    
    int ans = 0;
    for(auto val = val_set.crbegin(); val!=val_set.crend(); ++val){
        for(int status_i=0; status_i<STATUS_NUM; ++status_i){
            while(true){
                int nindex = next_indexs[status_i];
                if(nindex >= n){
                    break;
                }
                Element element = status_arrays[status_i][nindex];
                if(element.val < *val){
                    break;
                }
                status_flags[element.index] += 1 << status_i;
                satisfied_set.insert(status_flags[element.index]);
                next_indexs[status_i] += 1;
            }
        }
        for(auto a=satisfied_set.cbegin(); a!=satisfied_set.cend(); ++a){
            for(auto b=satisfied_set.cbegin(); b!=satisfied_set.cend(); ++b){
                for(auto c=satisfied_set.cbegin(); c!=satisfied_set.cend(); ++c){
                    if((*a | *b | *c ) == ((1 << STATUS_NUM) - 1)){
                        flag = true;
                        ans = *val;
                    }
                }
            }
        }
        if(flag){
            break;
        }
    }

    printf("%d\n", ans);
    return 0;
}