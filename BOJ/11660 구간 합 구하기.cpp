#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
int arr[1025][1025] = {};
int sumarr[1025][1025] = {};

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N(0), M(0),x1(0),y1(0),x2(0),y2(0);
	cin >> N;
	cin >> M;
	for (int i = 1; i <= N; i++) { //배열 입력받아오기
		for (int j = 1; j <= N; j++) cin >> arr[i][j];
	}

	for (int i = 1; i <= N; i++) { //합배열 만들기
		for (int j = 1; j <= N; j++) {
			sumarr[i][j] = sumarr[i - 1][j] + sumarr[i][j - 1] - sumarr[i - 1][j - 1] + arr[i][j];
		}
	}
	for (int i = 0; i < M; i++) {
		cin >> x1;
		cin >> y1;
		cin >> x2;
		cin >> y2;

		cout << sumarr[x2][y2] - sumarr[x1 - 1][y2] - sumarr[x2][y1 - 1] + sumarr[x1 - 1][y1 - 1]<<"\n";
	}
	
}
