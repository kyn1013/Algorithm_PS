#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N,sum(0);
	int A[50] = {};
	int B[50] = {};
	cin >> N;
	for (int i = 0; i < 50; i++) A[i] = 100;
	for (int i = 0; i < 50; i++) B[i] = 100;
	for (int i = 0; i < N; i++) cin >> A[i];
	for (int i = 0; i < N; i++) cin >> B[i];
	sort(A, A + 50);
	sort(B, B + 50);
	for (int i = 0,j=N-1; i < N; i++,j--) {
		sum += A[i] * B[j];
	}
	cout << sum;
}
