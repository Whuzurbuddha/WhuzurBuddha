
#include <iostream>

int main() {
    std::string word;
    std::cout << "Enter a word: " << std::endl;
    std::cin>> word;
    std::string fword= word;
    std::reverse(word.begin(), word.end());
    if (fword==word){
        std::cout<< fword << " is a palindrom.";
    }else{
        std::cout<< fword << " is not a palindrom.";
    }
    return 0;
}
