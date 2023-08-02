#include <iostream>
#include <locale.h>
using namespace std;

int main() {
  setlocale(LC_ALL, "portuguese");

  int senha, senha2;

  cout << "Digite a senha: " << endl;
  cin >> senha;
  cout << "Confirme a senha: " << endl;
  cin >> senha2;

  if(senha > 9999 || senha < 1000){

    cout << "Senha inválida, digite uma senha de 4 digitos por favor" << endl;

  }else{
    while (senha != senha2){
      cout << "Senha incorreta!" << endl;
      cin >> senha2;
    }
    cout << "Senha correta!" << endl;
  }


  return 0;
}
