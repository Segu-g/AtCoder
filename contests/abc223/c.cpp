#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    int *ab_array = new int[2 * n];
    for (int i = 0; i < n; i++)
    {
        std::cin >> ab_array[2 * i] >> ab_array[2 * i + 1];
    }
    double *sec = new double[n];
    double total = 0;
    double *cumsum_sec = new double[n];
    int *x_array = new int[n];
    int x = 0;
    for (int i = 0; i < n; i++)
    {
        int a = ab_array[2 * i];
        int b = ab_array[2 * i + 1];
        x += a;
        x_array[i] = x;
        total += (sec[i] = a / (double)b);
        cumsum_sec[i] = total;
    }
    const double target_sec = total / 2;
    int lo = 0;
    int hi = n;

    while (lo < hi)
    {
        int mid = (lo + hi) / 2;
        if (target_sec < cumsum_sec[mid])
            hi = mid;
        else
            lo = mid + 1;
    }

    double end_sec = cumsum_sec[lo];
    int end_len = x_array[lo];
    int b = ab_array[2 * lo + 1];

    std::cout << end_len - (end_sec - target_sec) * b << std::endl;
}