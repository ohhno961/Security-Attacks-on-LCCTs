#ifndef PRIVACYEXTRACTIONATTACK_H
#define PRIVACYEXTRACTIONATTACK_H

#include "Attack.h"
#include <string>

class PrivacyExtractionAttack : public Attack {
private:
    std::string query;
    
public:
    PrivacyExtractionAttack(std::string query);
    
    std::string getName() override;
    Prompt buildPrompt() override;
    AttackResult run() override;
};

#endif