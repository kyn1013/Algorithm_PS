#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N(0), count(0),a(97);
	int arr[26] = {}; //성의 첫 글자가 나온 횟수를 카운트하는 배열
	char aph[26] = {};
	
	cin >> N;
	for (int i = 0; i < N; i++) {
		string name;
		cin >> name;
		arr[name[0] - 'a']++;
	}
	for (int i = 0; i < 26; i++,a++) aph[i] = a;
	
	for (int i = 0; i < 26; i++) {
		if (arr[i] >= 5) {
			cout << aph[i];
			count++;
		}
	}
	if (count == 0) cout << "PREDAJA";
}
