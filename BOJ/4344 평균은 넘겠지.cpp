#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	cin.tie(0);
	int arr[1000] = {};
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int k(0),n(0);
		float average(0),sum(0),answer(0);
		cin >> n;
		for (int i = 0; i < n; i++) cin >> arr[i];
		for (int i = 0; i < n; i++) sum += arr[i];
		average = sum / n;
		for (int i = 0; i < n; i++) {
			if (arr[i] > average) k++;
		}
		answer = (float)k / n * 100;
		printf("%.3f%%\n", answer);
	}
	
}
