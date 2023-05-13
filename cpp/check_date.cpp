#include <iostream>

int main() {
    int day;
    int month;
    int year;
    std::cout << "Insert date: " <<std::endl;
    std::cin >> day >> month >> year;
    if  (((month==2) && ((year%4==0) && (day>0 && day<=29)) || (year%100!=0) && (day>0 && day <=28)) ||
         (((month == 4 || month == 6 || month == 9 || month == 11) && (day > 0 && day <= 30)) ||
          ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) &&
           (day > 0 && day <= 31)))){
        std::cout << day << "." << month << "." << year;
    }else{
        std::cout<< "this date does not exist";
    }
}
