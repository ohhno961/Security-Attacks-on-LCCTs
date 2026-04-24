/*
 * Prompt.h
 *
 * Data structure representing a single attack prompt.
 * Holds the original harmful query and the generated attack code.
 *
 * Author  : Aarush (Project Lead / Architecture)
 * Project : LCCT Security Attack Simulator
 * Paper   : "Security Attacks on LLM-based Code Completion Tools"
 *           Cheng et al., AAAI 2025 (arXiv:2408.11006)
 */

#ifndef PROMPT_H
#define PROMPT_H

#include <string>

// ------------------------------------------------------------
// Prompt
// Stores one entry from the dataset: the original harmful
// query Q and the generated attack code payload P.
// ------------------------------------------------------------
struct Prompt
{
    // The original harmful query (e.g., "How to produce counterfeit money?")
    std::string query;

    // The attack code payload constructed from the query.
    // This is what gets written to a .py file and fed to the LCCT.
    std::string attackCode;

    // Category tag: "illegal", "hate_speech", "pornography", "harmful"
    // Used to match Table 2 category breakdown in the paper.
    std::string category;

    // Simple constructor
    Prompt(const std::string& q, const std::string& cat)
        : query(q), attackCode(""), category(cat) {}
};

#endif // PROMPT_H
