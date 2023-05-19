#include <iostream>

int main() {
    std::cout << "Enter the number of calculations you want to do:  \n";
    float n = 0.0;
    std::cin>> n;
    float one = 1.0;
    float i = -1.0;
    float j = 1.0;
    int counter = 1.0;
    while(counter < n){
        i += 4.0;
        j += 4.0;
        one -= 1/i;
        one += 1/j;
        counter += 1;
    }
    std::cout << "Needed " << counter/4800000.0 << " seconds for calculation"  << "\n";
    float pi = one * 4;
    std::cout << "Pi: " << pi << "\n";
}
