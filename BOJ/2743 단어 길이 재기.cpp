#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;
int arr[1024][1024] = {};
int sumarr[1024][1024] = {};

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string str;
	int count(0);
	cin >> str;
	for (auto c : str) count++;
	cout << count;
}
