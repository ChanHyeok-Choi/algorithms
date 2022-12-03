#include <iostream>

int primes[50001] = { 0, }, cnt = 0;
// Sieve of Eratosthenes: O(Nlog(logN))
int* Algorithm(int* arr, int n) {
    for(int i = 0; i < n; i++) {
        int prime = arr[i];
        if(prime == 0 || prime == 1)
            continue;
        for(int j = i; j < n; j++) {
            if(arr[j] % prime == 0)
                arr[j] = 0;
        }
        primes[cnt++] = prime;
    }
    return primes;
}

void SetArray(int* arr, int n) {
    for(int i = 0; i < n; i++) {
        arr[i] = i+1;
    }
}

void printArray(int* arr, int n) {
    using namespace std;
    for(int i = 0; i < n; i++) {
        cout << arr[i] << ' ';
    }
    cout << '\n';
}

int main() {
    int arr[50001] = { 0, };
    int* answer;

    SetArray(arr, 5000); // { 1, 2, 3, 4, ..., 50000 }
    
    answer = Algorithm(arr, 5000);
    printArray(answer, cnt);

    return 0;
}