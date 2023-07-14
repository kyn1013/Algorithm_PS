#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int test;
	cin >> test;
	for (int i = 0; i < test; i++) {
		int store(0), ans(0);
		int location[100] = { 0 };
		cin >> store; //상점의 수 입력받기
		for (int i = 0; i < store; i++) cin >> location[i]; //각각의 위치 입력받기
		sort(location, location+store); //오름차순 정렬
		for(int i = 0; i<store - 1;i++) ans += abs(location[i+1] - location[i]);
		ans += abs(location[store-1] - location[0]);
		cout << ans<<"\n";
	}
}
