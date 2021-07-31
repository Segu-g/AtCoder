#include <iostream>

class MedianSqrtSplit{
    
}


int main(){
    int n, k;
    int** a_cells = new int*[n];
    int* buf = new int[n*n];
    for(int pos=0; pos<n*n; pos+=n){
        a_cells[row] = buf + pos;
    }

    for(int row=0; row<n; row++){
        for(int col=0; col<n; col++){
            std::cin >> a_cells[row][col];
        }
    }



    return 0;
}