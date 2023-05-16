#include <iostream>
#include <utility>

class Anschrift{
private:
    std::string address;
    int number;

public:
    explicit Anschrift(std::string ad = "", int nu = 0)
        : address(std::move(ad)), number(nu){}

    void printStrasse() const {
        std::cout << "Straße: " << address << std::endl;
        std::cout << "Nr: " << number << std::endl;
    }
};

class Person {
private:
    std::string name;
    int alter;
    std::string city;

public:
    // Konstruktor (move mindert das Kopieren von strings/ verbessert die Leistung)
    explicit Person(std::string n = "", int a = 0, std::string c = "")
            : name(std::move(n)), alter(a), city(std::move(c)) {}

    // Methoden
    void printName() const {
        std::cout << "Name: " << name << std::endl;
    }

    void printAlter() const{
        std::cout << "Alter: " << alter << std::endl;
    }

    void printCity() const{
        std::cout << "City: " << city << std::endl;
    }
};

void printInfo(const Person& person, const Anschrift& anschrift){ //konstante Referenz, statt das Objekt zu kopieren "(Person person)"
    person.printName();
    person.printAlter();
    anschrift.printStrasse();
    person.printCity();

}

void objects() {
    // Erstellung eines Objekts der Klasse Person
    Anschrift entenhausen("Fleischhauer-Straße",78);
    Anschrift hamburg("Müller-Alee", 12);
    Anschrift berlin("Gassenhauer-Straße", 33);

    Person person1("Max Mustermann", 30, "Hamburg");
    Person person2("Peter Lustig", 77, "Berlin");
    Person person3("Paula Knallkopf", 21, "Holliwutt");

    // Verwendung der Objektmethoden
    printInfo(person1, entenhausen);

    std:: cout << "\n" << std::endl;
    printInfo(person3, hamburg);

    std:: cout << "\n" << std::endl;
    printInfo(person2, berlin);

}
