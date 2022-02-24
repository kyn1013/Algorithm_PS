#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, N(-1),count(0);
	int a,b,c; //십의 자리, 일의 자리,각각의 합
	int k(-1);
	cin >> n;
	k = n;
	while (n != N) {
		if (k < 10) a = 0;
		else a = k / 10;
		b = k % 10;
		c = a + b;
		N = (b * 10) + (c%10);
		k = N;
		count++;
	}
	cout << count;
}
