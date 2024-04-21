#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int a,count,sum,sum2(0),k(0),h(1),count2(0);
	cin >> a;
	count = 2 * a - 1;
	count2 = count + 1;
	sum = count2;
	for (int i = 0; i <count; i++) {

		if (sum >= 1) {
			if (sum >= 2) {
				sum -= 2;
				for (int j = 0; j <= k; j++) cout << "*";
				for (int j = 0; j < sum; j++) cout << " ";
				for (int j = 0; j <= k; j++) cout << "*";
				k++;
			}
		}
		cout << "\n";
		if (sum == 0)  sum2 = sum,h=0,k--,sum--;
		if (h==0) {
				k--;
				sum2 = sum2 + 2;
				if (sum2 < count) {
					for (int j = 0; j <= k; j++) cout << "*";
					for (int j = 0; j < sum2; j++) cout << " ";
					for (int j = 0; j <= k; j++) cout << "*";
				}
			
		}
	}
}
