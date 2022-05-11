using namespace std;

#include <iostream>
#include <ctime>

int main() {

    int summa = 0, b = NULL, c = NULL;
    
    cout << "¬ведите числе b:";
    cin >> b;
    cout << "¬ведите числе c:";
    cin >> c;

    unsigned int start_time = clock();
    for (int i = 0; i < 100000000; i++) {
        summa += 2 * b + c - i;
    }

    unsigned int end_time = clock();
    unsigned int search_time = end_time - start_time;

    cout << "Function execution time:\n";
    cout << search_time << "ms\n";
    system("pause");
    return 0;
}