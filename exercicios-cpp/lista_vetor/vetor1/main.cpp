#include <iostream>
#include <locale.h>
using namespace std;


int main()
{
    setlocale(LC_ALL, "portuguese");

    int n[5];

    cout << "Digite os 5 n�meros: " << endl;

        for (int i = 0; i < 5; i++){
        cin >> n[i];
        }

    cout << "Os n�meros digitados foram: ";

        for (int i = 0; i < 5; i++){
        cout << n[i] << " ";
        }

    return 0;
}
