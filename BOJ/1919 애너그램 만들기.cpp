#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string stl1, stl2; //문자열 받아오기
	int count1[26] = {};
	int count2[26] = {}; //문자가 나온 횟수 카운트
	int def(0);
	cin >> stl1;
	cin >> stl2;

	for (auto c : stl1)  count1[c - 'a']++;
	for (auto c : stl2)  count2[c - 'a']++;
	for (int i = 0; i < 26; i++) {
		def += abs(count1[i] - count2[i]);
	}
	cout << def;
}
