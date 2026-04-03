#ifndef ATTACK_H
#define ATTACK_H

#include "Prompt.h"
#include "AttackResult.h"

// Attack is the abstract base class for all attack types
// Open/Closed Principle: open for extension (new attacks),
// closed for modification (base class stays the same)
class Attack {
public:
    // Every attack must be able to build its prompt
    // pure virtual = each subclass MUST implement this
    virtual Prompt buildPrompt() = 0;

    // Every attack must be able to run and return a result
    // pure virtual = each subclass MUST implement this
    virtual AttackResult run() = 0;

    // Returns the name of the attack
    // pure virtual = each subclass MUST implement this
    virtual std::string getName() = 0;

    // Virtual destructor: required for safe cleanup
    // when deleting objects through a base class pointer
    virtual ~Attack() {}
};

#endif