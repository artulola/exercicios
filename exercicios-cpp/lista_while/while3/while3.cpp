#include <iostream>
#include <locale.h>
using namespace std;

int main()
{
    setlocale(LC_ALL, "portuguese");

    int n;

    cout << "Digite os n�meros" << endl;

    while(true){
        cin >> n;
        if(n <= 1){
            cout << "N�mero menor ou igual a 1 encontrado!" << endl;
            break;
        }
    }


    return 0;
}
