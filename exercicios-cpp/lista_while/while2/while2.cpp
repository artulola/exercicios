#include <iostream>
#include <locale.h>
using namespace std;

int main()
{
    setlocale(LC_ALL, "portuguese");

    int n;
    int soma = 0;
    int valormedia = 0;
    int negativos = 0;
    int positivos = 0;

    cout << "Digite os n�meros (Digite 00 para sair): " << endl;

    while(true){
        cin >> n;

        if(n == 0){
            break;
        }

        soma += n;
        valormedia++;

        if (n < 0){
            negativos++;
        }else{
            positivos++;
        }
    }

    if(valormedia > 0){

        float media = soma*1.0/valormedia;
        float porpositivo = (positivos*1.0/valormedia) * 100;
        float pornegativo = (negativos*1.0/valormedia) * 100;

        cout << "M�dia: " << media << endl;
        cout << "Quantidade de n�meros positivos: " << positivos << endl;
        cout << "Porcentagem de n�meros positivos: " << porpositivo << "% " << endl;
        cout << "Quantidade de n�meros negativos: " << negativos << endl;
        cout << "Porcentagem de n�meros negativos: " << pornegativo << "% " << endl;
    }else{
        cout << "Nenhum n�mero foi digitado!" << endl;
    }



    return 0;
}
