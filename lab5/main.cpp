#include <iostream>
using namespace std;

double series(int n)
{
    if (n == 1)
    {
        return 1.0;
    }

    {
        if (n % 2 == 0)
        {
            return series(n - 1) - (1.0 / n);
        }

        {
            return series(n - 1) + (1.0 / n);
        }
    }
}

int main()
{
    int n;

    cout << "Enter n: ";
    cin >> n;

    cout << "Result: " << series(n) << endl;

    return 0;
}
