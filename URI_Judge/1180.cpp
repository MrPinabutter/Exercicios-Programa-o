#include <iostream>
using namespace std;

int main() {

  int n;
  cin >> n;

  int vetor[n];

  for(int i=0; i < n; i++) {     
    cin >> vetor[i]; 
 }

  int menor[2];

  menor[0] = 0;
  menor[1] = vetor[0];


  for(int i=0; i < n; i++){
    if(vetor[i] < menor[1]){
      menor[0] = i;
      menor[1] = vetor[i];
    }
  }

  cout << "Menor valor:" << menor[1] << endl;
  cout << "Posicao:" << menor[0] << endl;


  return 0;
}