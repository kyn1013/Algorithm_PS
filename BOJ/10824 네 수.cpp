#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	string A, B, C, D;
	cin >> A >> B >> C >> D;
	A = A + B;
	C = C + D;
	cout << stoll(A) + stoll(C);
}
