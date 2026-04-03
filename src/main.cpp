#include <iostream>
#include "Attack.h"
#include "Prompt.h"
#include "AttackResult.h"

// main.cpp is the entry point of the program
// Right now it just confirms the base framework is working
// Each new branch will add real attack classes here

int main() {

    // Print a welcome message to confirm the program runs
    std::cout << "==================================" << std::endl;
    std::cout << " LCCT Attack Framework Simulator" << std::endl;
    std::cout << "==================================" << std::endl;
    std::cout << "Base framework ready." << std::endl;
    std::cout << "No attacks loaded yet." << std::endl;

    return 0;
}