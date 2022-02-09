#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, k(0),set(1),six(0),min(0),sset(0);
	int a[10] = {}; //각 자릿수의 숫자를 담는 배열
	int b[8] = {}; //세트
	cin >> n;
	while (n != 0) {
		a[k] = n % 10;
		k++;
		n /= 10;
	}
	for (int i = 0; i < k; i++) {	
		if (a[i] == 0) b[0]++;
		else if (a[i] == 1) b[1]++;
		else if (a[i] == 2) b[2]++;
		else if (a[i] == 3) b[3]++;
		else if (a[i] == 4) b[4]++;
		else if (a[i] == 5) b[5]++;
		else if (a[i] == 6) six++;
		else if (a[i] == 7) b[6]++;
		else if (a[i] == 8) b[7]++;
		else if (a[i] == 9) six++;
	}
	six = six / 2+six%2; //6,9카운트
	sort(b, b + 8); //오름차순으로 정렬
	set = b[7];

	if (set < six) {
		for (int i = 0; i < six; i++) sset++;
	}
	else if (set > six) {
		for (int i = 0; i < set; i++) sset++;
	}
	else{
		for (int i = 0; i < set; i++) sset++;
	}

	cout << sset;
}
