#include <iostream>
#include <string>
using namespace std;

int main() {
  string str1, str2;
  int cont=0, maior=0;
  size_t found;

  while(getline(cin, str1)){
    getline(cin, str2);
    for(int i = 1; i <= str1.length(); i++){ 
      if(str2.length() < i)
        break;
      for(int j = 0; j <= str1.length()-i; j++){
        found = str2.find(str1.substr(j, i));
        if(found != std::string::npos) {
          if(i > maior)
            maior = i;
        }
      }
    }
    cout << maior << endl;
    maior = 0;
  }

  return 0;
}