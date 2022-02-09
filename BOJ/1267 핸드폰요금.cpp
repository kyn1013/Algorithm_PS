#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int a, b[20] = {},moneyY(0),moneyM(0),countY(0),countM(0),k(0);
	cin >> a;
	for (int i = 0; i < a; i++) cin >> b[i];
	
	
	for (int i = 0; i < a; i++) {
		countY = b[i] / 30;
		countM = b[i] / 60;
		for (int i = 0; i <= countY; i++) moneyY += 10;
		for (int i = 0; i <= countM; i++) moneyM += 15;
	}
	if (moneyY < moneyM) cout << "Y" << " " << moneyY;
	else if (moneyM < moneyY) cout << "M" << " " << moneyM;
	else if (moneyM == moneyY) cout << "Y" << " " << "M" <<" " << moneyM;
}
