#include <iostream>
#include<cstdlib>
using namespace std;

int main() {
    long num1, num2;
    long mul1(1),mul2(1),c,d,e,f;
    long ans(0),i(1),i2(1);

    cin >> num1;
    cin >> num2;

    if(num1 == 1) mul1 = 4;
    if(num2 == 1) mul2 = 4;

    while(num1 > mul1){ //4로 끊어주기
        mul1 = 4*i;
        i++;
    }
    while(num2 > mul2){
        mul2 = 4*i2;
        i2++;
    }

    c = mul1 - num1; 
    d = mul2 - num2; 
    ans += abs(c-d); //동서거리
    e = mul1 / 4;
    f = mul2 / 4;
    ans += abs(e-f); //남북거리
    cout << ans;
}
