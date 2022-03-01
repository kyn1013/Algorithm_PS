#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	char arr[100] = {};
	int k[10] = {}; //문자가 나온 횟수 0~9를 카운트
	int n,sum(0);
	cin >> n;
	for (int i = 0; i < n; i++) cin >> arr[i];
	for (int i = 0; i < n; i++) {
		k[arr[i] - '0']++;
	}
	for (int i = 0; i < 10; i++) {
		sum = sum + k[i] * i;
	}
	cout << sum;
}
