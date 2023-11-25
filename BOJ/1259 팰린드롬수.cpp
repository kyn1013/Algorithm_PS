#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    while (1) {
        string num;
        int ans(0);
        cin >> num;
        if (num == "0") break;
        if (num.length() % 2 == 1) { //문자열의 길이가 홀수인 경우
            int mid = num.length() / 2; //문자열의 중간값 인덱스
            char add[1] = {}, min[1] = {}; //비교할 문자를 담을 문자
            int k = mid;
            for (int i = mid - 1; i >= 0; i--) {
                min[0] = num[i];
                k++;
                add[0] = num[k];
                if (add[0] != min[0]) ans = 1;
            }
        }
        else { //짝수인 경우
            int mid = num.length() / 2 - 1; //문자열의 중간값 인덱스
            char add[1] = {}, min[1] = {}; //비교할 문자를 담을 문자
            int k = mid;
            for (int i = mid; i >= 0; i--) {
                min[0] = num[i];
                k++;
                add[0] = num[k];
                if (add[0] != min[0]) ans = 1;
            }
        }
        if (ans == 1) cout << "no"<<"\n";
        else cout << "yes"<<"\n";
    }
    
}
