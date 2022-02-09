#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
int a[1000000]; //자연수를 담는 배열
int occur[2000000]; //자연수가 나온 횟수를 담는 배열
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int n, x,count(0);
	cin >> n;
	for (int i = 0; i < n; i++) cin >> a[i];
	cin >> x;

	for (int i = 0; i < n; i++) {
		if (x-a[i]>0&&occur[x - a[i]] == 1) count++;
		else occur[a[i]] = 1;
	}

	cout << count;
}
