#include <bits/stdc++.h>
using namespace std;

long long N(0), M(0); //강의실 개수, 예약 개수
long long endtime[200001] = {}; //각 강의실마다 끝난 시간을 담는 배열
long long num(0), s(0), e(0); //강의실 번호, 시작시간, 끝시간

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	for (long long i = 0; i < 200001; i++) endtime[i] = 0;

	cin >> N >> M;
	for (long long i = 0; i < M; i++) {
		cin >> num >> s >> e; // 1 2 5 , 1 6 8
		if (endtime[num] == 0) {
			endtime[num] = e;
			cout << "YES\n";
		}
		else {
			if (s >= endtime[num]) { cout << "YES\n"; endtime[num] = e; }
			else cout << "NO\n";
		}
	}
}
