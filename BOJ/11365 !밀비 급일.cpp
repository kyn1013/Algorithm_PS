#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	while (1) {
		string str;
		getline(cin,str);
		if (str == "END") break;
		cin.clear();
		for (int i = str.length()-1; i >= 0; i--) {
			cout << str[i];
		}
		cout << "\n";
	}
}
