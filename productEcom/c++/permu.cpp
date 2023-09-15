#include<iostream>
using namespace std; 
void merge( int a[], int si, int mid, int end ){
    int i=si; 
    int j=mid+1;
    int r[100];
    int p=si;
    while(i<=mid&&j<=end){
        if(a[i]<a[j]){
r[p++]=a[i++];
        }
        else{r[p++]=a[j++];}
    }
    while(i<=mid){
        r[p++]=a[i++];
    }
    while(j<=end){
        r[p++]=a[i++];
    }
    for(int x=si; x<=end; x++){
        a[si]=r[si];
    }
}
int merge_soty(int a[], int si, int end){
    if(si>=end){
        return ;
    }
    int mid=(si+end)/2;
    merge_soty(a, si,mid);
    merge_soty(a,mid+1,end);
    merge(a,si, mid, end);

    }
    int main(){
        int a[100];
         int n; 
         cin>>n;
          for(int i=0 ; i<n; i++){
             cin>>a[i];
          }
          int si=0; 
          int end =n-1;
          merge_soty(a, si, end);
          for(int i=0 ;i<n; i++){
            cout<<a[i];
          }
    }