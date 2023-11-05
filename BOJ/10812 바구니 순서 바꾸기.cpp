#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N,M; //바구니 개수, 돌릴 횟수
    int arr[100] = {};

    cin >> N >> M;

    for (int i = 1; i <= N; i++) {
        arr[i] = i;  // 1 2 3 4 5
    }

    for (int d = 0; d < M; d++) {
        int a, b, c, k; //시작, 끝, 기준, 끝 값을 담을 변수
        cin >> a >> b >> c;

        for (int i = c; i > a; i--) {
            k = arr[b]; //끝값 담기
            arr[b] = arr[a]; //처음값을 끝값으로 이동
            for (int j = a + 1; j < b; j++) { //끝값 -1부터 한칸씩 앞으로 이동
                arr[j - 1] = arr[j];
            }
            arr[b - 1] = k; //끝값 -1에 끝값넣기
            }
        
    }
  
    for (int i = 1; i <= N; i++) cout << arr[i] << " ";
}
