#include <cstdio>
#include <time.h>
#include <queue>

template <class Type,
          class Compare = less<typename Container::value_type>>
class Heapq{
public:
    Heapq(int max_length, int length, Type* array);
    ~Heapq(){}
    void replace(int index, Type value);
    int append(Type value);
private:
    void _shiftdown(int pos);
    void _shiftup(int pos);
    Type* val_array;
    int* index_heapq;
    int size;
};

template <class Type,
          class Compare = less<typename Container::value_type>>
Heapq<Type,Compare>::Heapq(int max_length, int length, Type* array){
    this.val_array = new Type[max_length];
    this.index_heapq = new int[max_length];

}


Heapq::

int main(void){
    int id, n, k;
    scanf("%d %d %d", &id, &n, &k);
    int *row, *col;
    row =  new int[k*n];
    col = new int[k*n];
    char** cell = new char*[n];
    for(int i=0; i<n; i++){
        cell[i] = new char[n];
    }
    for(int i=0; i<n; i++){
        scanf("%s",cell[i]);
        for(int j=0; j<n; j++){
            cell[i][j] -= '1';
            row[i*k + (int)cell[i][j]] += 1;
            col[j*k + (int)cell[i][j]] += 1;
        }
    }
    priority_queue<std::pair<int, int>,
                   std::vector<std::pair<int, int>>,
                   CompareByFirst>* row_que;
    priority_queue<std::pair<int, int>,
                   std::vector<std::pair<int, int>>,
                   CompareByFirst>* col_que;

    row_que = new priority_queue<std::pair<int, int>,
                   std::vector<std::pair<int, int>>,
                   CompareByFirst>[k];
    col_que = new priority_queue<std::pair<int, int>,
                   std::vector<std::pair<int, int>>,
                   CompareByFirst>[k];

    for(int i=0; i<n; i++){
        for(int c=0; c<k; c++){
            row_que[c].push(std::make_pair(row[i*k + c], i));
            col_que[c].push(std::make_pair(col[i*k + c], i));
        }
    }
}
