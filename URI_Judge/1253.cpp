#include <iostream>
#include <string>
using namespace std;

int main() {

  int n, des;
  string text;

  cin >> n;

  for(int i=0; i < n; i++) {   
    cin >> text;
    cin >> des;
    for(char letter: text){
      if(int(letter) - des < 65){
        cout << char(int(letter)-des+26);
      }else{
        cout << char(int(letter)-des);
      }
    }
    cout << endl;
  }
  return 0;
}