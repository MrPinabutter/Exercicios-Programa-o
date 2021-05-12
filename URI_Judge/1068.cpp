#include <iostream>
#include <string>
using namespace std;

int main() {
  string word;
  int abre, fecha;
  while(getline(cin, word)){
    abre = 0, fecha = 0;
    for(char letter: word) {
      if(letter == '(')
        abre++;
      if(letter == ')'){
        if(fecha + 1 > abre){
          fecha = -1;
          break;
        }
        fecha++;
      }
    }

    if(abre == fecha) {
      cout << "correct" << endl;
    }else {
      cout << "incorrect" << endl;
    }
  }

  return 0;
}