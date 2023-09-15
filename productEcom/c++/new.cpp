#include<iostream>
using namespace std;
 void sew(string input, string output){
    if(input.size()==0){
        cout<<output<<endl;
        return ;
    }
    sew(input.substr(1), output);
    sew(input.substr(1),input[0]+output);
 }
 int main(){
    string ni;
     cin>>ni;
     string output;
      sew(ni, output);
 }