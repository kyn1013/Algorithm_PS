#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(0);
	string k;
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int score(0),num(0);
		cin >> k;
		for (auto c:k) {
			if (c == 'O') {
				score++;
				num += score;
			}
			else score = 0;
		}
		cout << num<<"\n";
	}
}
