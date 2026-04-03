#include <iostream>
#include "Attack.h"
#include "Prompt.h"
#include "AttackResult.h"
#include "PrivacyExtractionAttack.h"

// main.cpp is the entry point of the program
// This demonstrates the PrivacyExtractionAttack implementation

int main() {
    std::cout << "==========================================" << std::endl;
    std::cout << "  LCCT Privacy Extraction Simulator " << std::endl;
    std::cout << "==========================================" << std::endl;

    // The target is a specific platform known for proprietary training data
    std::string targetPlatform = "GitHub";
    
    // Instantiate the attack logic
    Attack* attack = new PrivacyExtractionAttack(targetPlatform);
    
    std::cout << "Running two-step extraction process..." << std::endl;
    Prompt prompt = attack->buildPrompt();
    AttackResult result = attack->run();
    
    // Display findings
    std::cout << "\n--- Attack Results ---" << std::endl;
    std::cout << "Attack Name : " << result.getAttackName() << std::endl;
    std::cout << "Success     : " << (result.isSuccess() ? "YES" : "NO") << std::endl;
    std::cout << "Response    : " << result.getResponse() << std::endl;

    delete attack;
    return 0;
}