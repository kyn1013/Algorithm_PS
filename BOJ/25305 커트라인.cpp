#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, k; //응시자 수, 상을 받는 사람 수
    int score[1000] = {};

    cin >> N >> k;
    for (int i = 0; i < N; i++) {
        cin >> score[i];
    }
    sort(score, score + 1000, greater<>()); //내림차순
    cout << score[k-1];
}
