#include <iostream>
#include <string.h>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;

struct feira {
  string name;
  double value;
};

int main() {
  int n, qtd;
  vector<feira> items;
  
  cin >> n;

  for(int i=0; i < n; i++) {
    cin >> qtd;

    for(int j=0; j < qtd; j++){
      string name;
      double value;
      cin >> name;
      cin >> value;

      feira nova = {name, value};

      items.push_back(nova);
    }
    
    cin >> qtd;
    double sum = 0;
    for(int j=0; j < qtd; j++){
      string name;
      int num;
      cin >> name;
      cin >> num;

      for(feira i: items) {
        if (name == i.name){
          sum +=i.value*num;
        }
      }
    }
    cout << "R$ ";
    cout << fixed << setprecision(2);
    cout << sum << endl;
    items.clear();
  }

  return 0;
}