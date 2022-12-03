#include <iostream>

using namespace std;

int EuclideanAlgorithm(int a, int b) {
    while(b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    int a, b;
    cout << "Input your two integers for GCD: "; cin >> a >> b;

    cout << "Greatest Common Divisor (" << a << ", " << b <<"): " << EuclideanAlgorithm(a, b) << '\n';

    return 0;
}