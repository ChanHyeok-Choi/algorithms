/* Writer: 20181257 ChanHyeok Choi
Date: 2023-05-06

6. (2 points) Given an array A consisting of n positive integers, let's assume that we want to find a
positive integer k such that the total sum of the distances between all elements of A and k
becomes minimized, i.e., sum = min ∑ d_i from i=1 to n , where d_i = |A[i] - k| is the distance between A[i] and
k. Write real code (not pseudocode) that returns sum (not k), given an array A of length n. Write
(type) your code with a keyboard and upload it as a separate file.
● Your code should be written either in C or Python. It should be compiled and run (Zero points if
the uploaded code does not run).
● Do not use built-in C or Python libraries that directly solve the problem.
● Upload your code as a separate file
● Only the code uploaded to BlackBoard will be graded (not the code on your computer).*/

#include <iostream>

int partition(int *A, int p, int r) {
    int x = A[r];
    int i = p-1;

    for (int j = p; j <= r-1; j++) {
        if (A[j] <= x) {
            i++;
            // exchange A[i] with A[j]
            int temp = 0;
            temp = A[j];
            A[j] = A[i];
            A[i] = temp;
        }
    }
    // exchange A[i+1] with A[r]
    int temp = 0;
    temp = A[r];
    A[r] = A[i+1];
    A[i+1] = temp;

    return i+1;
}

void quick_sort(int *A, int p, int r) {
    if (p < r) {
        int q = partition(A, p, r);
        quick_sort(A, p, q-1);
        quick_sort(A, q+1, r);
    }
}

int sum_dist_twoFor(int *A, int n) {
    int sum = 0;
    // Your code
    quick_sort(A, 0, n-1);

    int maximum = 0;
    for (int i = 0; i < n; i++) {
        maximum += A[i];
    }

    sum = maximum;
    for (int i = 0; i < n; i++) {
        int sum_i = 0;
        for (int j = 0; j < n; j++) {
            sum_i += abs(A[j] - i);
        }
        sum = (sum < sum_i ? sum : sum_i);
    }

    return sum;
}

int sum_dist_median(int *A, int n) {
    int sum = 0;
    // Your code
    quick_sort(A, 0, n-1);

    int median = A[(int) n/2];
    for (int i = 0; i < n; i++) {
        sum += abs(A[i] - median);
    }
    return sum;
}

bool Test_sum_dist(int *A, int n) {
    return sum_dist_twoFor(A, n) == sum_dist_median(A, n);
}

int main() {
    int A1[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int A2[8] = {2, 8, 7, 1, 3, 5, 6, 4};
    int A3[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 10};
    int A4[9] = {1, 1, 1, 1, 1, 1, 1, 1, 10};
    int A5[10] = {1, 1, 1, 1, 1, 1, 2, 1, 2, 10};
    int A6[10] = {10, 10, 10, 10, 10, 9, 2, 1, 2, 1};
    
    // quick_sort(A1, 0, 7);
    
    // for (int i = 0; i < 8; i++) {
    //     std::cout << A1[i] << " ";
    // }

    std::cout << Test_sum_dist(A1, sizeof(A1)/sizeof(*A1)) << '\n';
    std::cout << Test_sum_dist(A2, sizeof(A2)/sizeof(*A2)) << '\n';
    std::cout << Test_sum_dist(A3, sizeof(A3)/sizeof(*A3)) << '\n';
    std::cout << Test_sum_dist(A4, sizeof(A4)/sizeof(*A4)) << '\n';
    std::cout << Test_sum_dist(A5, sizeof(A5)/sizeof(*A5)) << '\n';
    std::cout << Test_sum_dist(A6, sizeof(A6)/sizeof(*A6)) << '\n';

    return 0;
}