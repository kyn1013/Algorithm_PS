#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int arr[10] = {}; //입력받을 수를 담을 배열
	int remain[10] = {}; //입력받은 수를 42로 나눈 나머지를 담을 배열
	int count[1000] = {}; //나머지인 수들의 횟수를 카운트하는 배열
	int c(0);
	for (int i = 0; i < 10; i++) cin >> arr[i];
	for (int i = 0; i < 10; i++) remain[i] = arr[i] % 42;
	for (int i = 0; i < 10; i++) {
		count[remain[i]]++;
	}
	for (int i = 0; i < 1000; i++) {
		if (count[i] != 0) c++;
	}
	cout << c;

}
