#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int a,sum(1),count(0),k(1),m(0);
	cin >> a;
	count = (a * 2 - 1)/2;
	for (int i = 0; i < a*2-1; i++) {
		if (count >= 0) {
			for (int j = 0; j < count; j++) cout << " ";
			count--;
			for (int i = 1; i <= sum; i++) cout << "*";
			sum += 2;
		}
		cout << "\n";
		
		if (count<0) {
			if (m == 0) {
				sum = sum - 2;
				m = 1;
			}
			sum = sum - 2;
			for (int i = 0; i < k; i++) cout << " ";
			k++;
			for (int i = 1; i <= sum; i++) cout << "*";
		}

	}

}
