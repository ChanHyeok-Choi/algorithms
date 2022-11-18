#include <iostream>
#include <string>

int CorrectCommand(std::string text) {
    if (text.length() != 7)
        return 0;
    
    if (text[0] == text[1] && text[0] == text[1] && text[6] == text[2] && text[6] == text[3] && text[6] == text[5] && text[0] != text[6])
        return 1;
    else
        return 0;
}

int main() {
    using namespace std;
    
    int n; cin >> n;
    for(int i = 0; i < n; i++) {
        string text;
        cin >> text;
        cout << CorrectCommand(text) << endl;
    }

    return 0;
}