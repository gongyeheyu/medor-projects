#include <iostream>
using namespace std;
int main()
{
    cout << "input your age:" << endl;
    int age;
    cin >> age;
    int mon = age*12;
    cout << endl << "you have lived for " << mon << " mounth";
    cin.get();
    cin.get();
    return 0;
}