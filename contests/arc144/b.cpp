#include <iostream>

int main() {
    int64_t n, a, b;
    std::cin >> n >> a >> b;
    int64_t* a_arr = new int64_t[n];
    for (size_t i=0; i<n; i++) {
        std::cin >> a_arr[i];
    }

    int64_t left, right, middle;
    left = a_arr[0];
    right = a_arr[0] + 1;
    for (size_t i=0; i<n; i++) {
        left = std::min(a_arr[i], left);
        right = std::max(a_arr[i] + 1, right);
    }

    while (left < right) {
        middle = (right + left) / 2;
        int64_t pluse = 0;
        int64_t minus = 0;
        for (size_t i=0; i<n; i++) {
            const int64_t diff = a_arr[i] - middle;
            if (diff >= 0) {
                pluse += diff / b;
            } else {
                minus += (- diff + a - 1) / a;
            }
        }

        // std::cout << middle << ": " << pluse - minus << std::endl;


        if (pluse >= minus) {
            left = middle + 1;
        } else {
            right = middle;
        }
    }

    std::cout << left - 1 << std::endl;

    return 0;
}
