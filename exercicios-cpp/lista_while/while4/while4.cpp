#include <iostream>
#include <locale.h>
using namespace std;

int main()
{
    setlocale(LC_ALL, "portuguese");

    int n, soma;

    cout << "Digite os n�meros: " << endl;

    while(true){
        cin >> n;

        soma += n;

        if(n == 0){
            break;
        }
    }

    cout << "Soma dos n�meros digitados: " << soma << endl;





    return 0;
}
