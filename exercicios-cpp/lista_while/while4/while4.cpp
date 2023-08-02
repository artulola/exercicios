#include <iostream>
#include <locale.h>
using namespace std;

int main()
{
    setlocale(LC_ALL, "portuguese");

    int n, soma;

    cout << "Digite os números: " << endl;

    while(true){
        cin >> n;

        soma += n;

        if(n == 0){
            break;
        }
    }

    cout << "Soma dos números digitados: " << soma << endl;





    return 0;
}
