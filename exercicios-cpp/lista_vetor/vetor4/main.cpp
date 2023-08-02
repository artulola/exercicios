#include <iostream>
#include <locale.h>
using namespace std;

int main()
{
    setlocale(LC_ALL, "portuguese");

    int idade[5];
    float altura[5];

    cout << "Digite a idade e a altura das 5 pessoas, respectivamente: " << endl;

    for(int i = 0; i < 5; i++){
        cout << "Digite a idade: ";
        cin >> idade[i];
        cout << "Digite a altura: ";
        cin >> altura[i];
    }

    cout << "Idades e alturas digitadas em ordem invertida" << endl;

    for (int i = 4; i >= 0; i--){
        cout << idade[i] << " ";
    }

    for (int i = 4; i >= 0; i--){
        cout << altura[i] << " ";
    }




    return 0;
}
