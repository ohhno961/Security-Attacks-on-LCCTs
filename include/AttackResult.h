#ifndef ATTACKRESULT_H
#define ATTACKRESULT_H

#include <string>

// AttackResult class stores the outcome of one attack attempt
// Single Responsibility: only holds result data, nothing else
class AttackResult {
private:
    std::string attackName;   // name of the attack that was used
    std::string response;     // simulated response from the LCCT
    bool success;             // true if attack succeeded, false if not

public:
    // Constructor: sets all result data at once
    AttackResult(std::string attackName, std::string response, bool success)
        : attackName(attackName), response(response), success(success) {}

    // Returns the name of the attack
    std::string getAttackName() const {
        return attackName;
    }

    // Returns the simulated LCCT response
    std::string getResponse() const {
        return response;
    }

    // Returns true if the attack was successful
    bool isSuccess() const {
        return success;
    }
};

#endif