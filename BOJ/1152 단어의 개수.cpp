#pragma warning(disable:4996)
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int count(0);
    getline(cin,s);
      
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') count++;
    }
    if (s[0] == ' ') count--;
    if (s[s.length() - 1] != ' ') count++;
    cout << count;
}
