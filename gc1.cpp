// glitch.cpp
// compile: g++ -O2 -std=c++17 glitch.cpp -o glitch
#include <iostream>
#include <iomanip>
#include <random>
#include <chrono>
#include <thread>
#include <string>

using namespace std;
using namespace std::chrono_literals;

string randhex(size_t n) {
    static const char *hex = "0123456789abcdef";
    static std::mt19937_64 rng((unsigned)chrono::high_resolution_clock::now().time_since_epoch().count());
    string s; s.reserve(n);
    for(size_t i=0;i<n;i++) s.push_back(hex[rng()%16]);
    return s;
}

void slow(const string &t, int ms=6) {
    for(char c: t) {
        cout << c << flush;
        this_thread::sleep_for(std::chrono::milliseconds(ms));
    }
    cout << endl;
}

int main(){
    cout << "\033[1;36m" << "=== BLACK-BOX GLITCH CONSOLE ===" << "\033[0m" << endl;
    this_thread::sleep_for(300ms);
    for(int i=0;i<6;i++){
        cout << "\033[1;35m" << randhex(48) << "\033[0m" << endl;
        this_thread::sleep_for(80ms);
    }
    cout << "\n";
    string art =
    "     .----.    .----.    .----.\n"
    "    / .--. \\  / .--. \\  / .--. \\\n"
    "   / /    \\ \\/ /    \\ \\/ /    \\ \\\n"
    "  | |      | || |      | || |      |\n"
    "   \\ \\    / /\\ \\    / /\\ \\    / /\n"
    "    '.__.'\"  '.__.'\"  '.__.'\"\n";
    slow(art, 2);
    cout << "\033[33m" << "scanning memory regions..." << "\033[0m" << endl;
    for(int base=0x7fff0000; base<0x7fff0120; base+=0x10){
        cout << hex << showbase << setw(10) << base << " : " << randhex(16) << endl;
        this_thread::sleep_for(40ms);
    }
    cout << dec << nouppercase << endl;
    cout << "\033[31m" << "!!! WARNING: UNUSUAL PATTERN DETECTED !!!" << "\033[0m" << endl;
    for(int i=0;i<3;i++){
        cout << "\033[1;30;47m" << " 0x" << randhex(8) << "  ::  " << randhex(32) << "\033[0m" << endl;
        this_thread::sleep_for(120ms);
    }
    cout << "\n";
    cout << "\033[32m" << "dump saved to /tmp/.shadow-dump-" << randhex(6) << "\033[0m" << endl;
    cout << "\033[2m" << "press Ctrl-C to quit the theatrical console..." << "\033[0m" << endl;
    // keep printing noise until user stops
    while(true){
        cout << randhex(40) << "  " << randhex(8) << endl;
        this_thread::sleep_for(220ms);
    }
    return 0;
}
