#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int n(0),k(0);
    int arr[10000]={};//약수를 담는 배열
    for(int i=0;i<10000;i++){
        arr[i]=999999;
    }
    cin>>n;
    cin>>k;
    for(int i=1;i<10000;i++){
        if(n%i==0) arr[i]=i;
    }
    sort(arr,arr+10000);
    if(arr[k-1]==999999)cout<<0;
    else cout<<arr[k-1];
}
