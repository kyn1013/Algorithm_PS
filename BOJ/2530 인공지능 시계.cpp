#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long sec, min, hour, time, Asec(0), Amin(0), Ahour(0);
	cin >> hour >> min >> sec;
	cin >> time;
	Amin = (sec + time) / 60;
	Asec = (sec + time) % 60;
	Ahour = (Amin + min) / 60+hour;
	Amin = (Amin + min) % 60;
	if (Ahour > 23) {
		Ahour = Ahour%24;
	}
	cout << Ahour << " " << Amin << " " << Asec;
}
