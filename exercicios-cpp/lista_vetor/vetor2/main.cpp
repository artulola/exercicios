#include <iostream>
#include <locale.h>
using namespace std;


int main()
{
    setlocale(LC_ALL, "portuguese");

    float n[10];

        cout << "Digite os n�meros reais: " << endl;

    for (int i = 0; i < 10; i++){
        cin >> n[i];
    }

        cout << "Os n�meros digitados em ordem invertida s�o: " << endl;

    for (int i = 9; i >= 0; i--){
        cout << n[i] << " ";
    }


    return 0;
}
