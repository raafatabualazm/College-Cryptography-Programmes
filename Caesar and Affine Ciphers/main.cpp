#include <iostream>
#include <map>
#include <string>
using namespace std;
map<int, int> inverses;
string CaesarEncrypt(string plaintext, int b) {
    string ciphertext;
    char pc;
    char cc;
    b = b % 26;
    for (int i = 0; i < plaintext.length(); i++)
    {
        pc = plaintext[i] - 'a';
        cc = (pc + (b)) % 26;
        cc = cc + 'a';
        ciphertext.push_back(cc);
    }
    return ciphertext;
}

string CaesarDecrypt(string ciphertext, int b) {
    string plaintext;
    char pc;
    char cc;
    b = b % 26;
    b = (b == 0) ? 0 : 26 - b;
    for (int i = 0; i < ciphertext.length(); i++)
    {
        cc = ciphertext[i] - 'a';
        pc = (cc + (b)) % 26;
        pc = pc + 'a';
        plaintext.push_back(pc);
    }
    return plaintext;
}

string AffineEncrypt(string plaintext, int a, int b) {
    string ciphertext;
    char pc;
    char cc;
    a = a % 26;
    b = b % 26;
    for (int i = 0; i < plaintext.length(); i++)
    {
        pc = plaintext[i] - 'a';
        cc = ((a*pc)%26 + (b)) % 26;
        cc = cc + 'a';
        ciphertext.push_back(cc);
    }
    return ciphertext;
}

string AffineDecrypt(string ciphertext, int a, int b) {
    string plaintext;
    char pc;
    char cc;
    a = a % 26;
    b = b % 26;
    a = inverses[a];
    b = (b == 0) ? 0 : 26 - b;
    for (int i = 0; i < ciphertext.length(); i++)
    {
        cc = ciphertext[i] - 'a';
        pc = ((a)*(cc + b)) % 26;
        pc = pc + 'a';
        plaintext.push_back(pc);
    }
    return plaintext;
}
int main() {
    inverses[1] = 1;
    inverses[3] = 9;
    inverses[5] = 21;
    inverses[7] = 15;
    inverses[9] = 3;
    inverses[11] = 19;
    inverses[15] = 7;
    inverses[17] = 23;
    inverses[19] = 11;
    inverses[21] = 15;
    inverses[23] = 17;
    inverses[25] = 25;
    cout << "Enter text to Encrypt or Decrypt: " << endl;
    string text;
    int a, b;
    cin >> text;
    cout << "Do you want Encryption or Decryption: " << endl;
    string encdec;
    string method;
    cin >> encdec;
    if (encdec == "dec" || encdec == "Dec" || encdec == "DEC" || encdec == "d" || encdec == "D" || encdec == "Decryption" || encdec == "decryption")
    {
        cout << "Do you want Caesar or Affine Algorithm? " << endl;
        cin >> method;
        if (method == "Affine" || method == "affine" || method == "a" || method == "A")
        {
            cout << "Enter a and b the key parameters: " << endl;
            cin >> a >> b;
            cout << AffineDecrypt(text, a, b);

        } else if (method == "Caesar" || method == "caesar" || method == "c" || method == "C")
        {
            cout << "Enter b the key parameter: " << endl;
            cin >> b;
            cout << CaesarDecrypt(text, b);
        }
    }
    else if (encdec == "enc" || encdec == "Enc" || encdec == "ENC" || encdec == "e" || encdec == "E" || encdec == "Encryption" || encdec == "encryption")
    {
        cout << "Do you want Caesar or Affine Algorithm? " << endl;
        cin >> method;
        if (method == "Affine" || method == "affine" || method == "a" || method == "A")
        {
            cout << "Enter a and b the key parameters: " << endl;
            cin >> a >> b;
            cout << AffineEncrypt(text, a, b);

        } else if (method == "Caesar" || method == "caesar" || method == "c" || method == "C")
        {
            cout << "Enter b the key parameter: " << endl;
            cin >> b;
            cout << CaesarEncrypt(text, b);
        }
    }
    return 0;
}
