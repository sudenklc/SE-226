#include <iostream>
using namespace std;

void swapValues(int* p1, int* p2) {
    int temp = *(p1);
    *(p1) = *(p2);
    *(p2) = temp;
}
void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i) << " ";
    }
    cout << endl;
}
int findSum(int* arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += *(arr + i);
    }
    return sum;
}
void shiftRight(int* arr, int size) {
    if (size <= 1) {
        return;
    }
    int last = *(arr + size - 1);

    for (int i = size - 1; i > 0; i--) {
        *(arr + i) = *(arr + i - 1);
    }
    *arr = last;
}
int* createArray(int size) {
    int* arr = new int[size];
    return arr;
    }

void deleteArray(int* arr) {
    delete[] arr;
}
int main() {
    cout << "creating dynamic array" << endl;
    int size;
    cout << "enter size of array: ";
    cin >> size;
    int* arr = createArray(size);
    cout << "enter values for arrays: ";
    for (int i = 0; i < size; i++) {
        cin >> *(arr + i);
    }
    cout << "array elements: " << endl;
    printArray(arr, size);
    cout << "sum of elements: " << findSum(arr, size) << endl;
    cout << "swapping elements: " << endl;
    int a, b;
    cout << "enter element a: ";
    cin >> a;
    cout << "enter element b: ";
    cin >> b;
    cout << "before swap" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    swapValues(&a, &b);
    cout << "after swap" << endl;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    cout << "shifting array to the right"<< endl;
    shiftRight(arr, size);
    cout << "after shifting" << endl;
    printArray(arr, size);
    cout << "deleting array" << endl;
    deleteArray(arr);
    cout << "memory erased successfully" << endl;
    return 0;

}

