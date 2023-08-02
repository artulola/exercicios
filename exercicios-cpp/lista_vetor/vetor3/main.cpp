#include <iostream>
#include <locale.h>

using namespace std;

int main()
{
    setlocale(LC_ALL, "portuguese");

    int notas[4], soma, media;

    cout << "Digite as notas do aluno: " << endl;

    for(int i = 0; i < 4; i++){
        cin >> notas[i];
        soma += notas[i];
    }

    cout << "Essas foram as notas digitadas: " << endl;
    for(int i = 0; i < 4; i++){
        cout << notas[i] << " ";
    }

    cout << endl;

    media = soma/4;

    cout << "Média final do aluno: " << media << endl;




    return 0;
}
