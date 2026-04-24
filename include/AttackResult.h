/*
 * AttackResult.h
 *
 * Holds the result of running one attack on one prompt.
 * Tracks success/failure and the generated attack file path
 * so the Python automation layer knows where to pick up the file.
 *
 * Author  : Aarush (Project Lead / Architecture)
 * Project : LCCT Security Attack Simulator
 * Paper   : "Security Attacks on LLM-based Code Completion Tools"
 *           Cheng et al., AAAI 2025 (arXiv:2408.11006)
 */

#ifndef ATTACK_RESULT_H
#define ATTACK_RESULT_H

#include <string>

// ------------------------------------------------------------
// AttackResult
// Returned by every concrete Attack subclass after generating
// one attack prompt file. The Python layer reads the file at
// outputFilePath and feeds it to the target LCCT.
// ------------------------------------------------------------
struct AttackResult
{
    // True if the attack file was successfully generated.
    // Does NOT mean the LCCT was jailbroken — that evaluation
    // happens in the Python layer (see research_repo/).
    bool generated;

    // Absolute path to the generated .py attack file.
    std::string outputFilePath;

    // The original query this result corresponds to.
    std::string originalQuery;

    // Human-readable description of what was built.
    std::string description;

    // Default: not generated yet
    AttackResult()
        : generated(false), outputFilePath(""), originalQuery(""), description("") {}
};

#endif // ATTACK_RESULT_H
