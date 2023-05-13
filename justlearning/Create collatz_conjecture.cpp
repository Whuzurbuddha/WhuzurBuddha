#include <iostream>

int main() {
    std::cout << "Enter a number: " << std::endl;
    int input;
    std::cin >> input;
    while (input != 1){
        if (input % 2 != 0){
            input = (input * 3) + 1;
        }else if(input % 2 == 0){
            input = input / 2;
        }
        std::cout << input << " ";
    }
}
