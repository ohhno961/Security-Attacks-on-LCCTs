/*
 * Attack.h
 *
 * Abstract base class for all LCCT attack strategies.
 * Every concrete attack (FilenameProxy, CrossFile, Hierarchical,
 * PrivacyExtraction) inherits from this class.
 *
 * Design follows the Open/Closed Principle:
 *   - Open for extension  : add a new attack by subclassing Attack.
 *   - Closed for modification : Attack.h itself never changes.
 *
 * Author  : Aarush (Project Lead / Architecture)
 * Project : LCCT Security Attack Simulator
 * Paper   : "Security Attacks on LLM-based Code Completion Tools"
 *           Cheng et al., AAAI 2025 (arXiv:2408.11006)
 */

#ifndef ATTACK_H
#define ATTACK_H

#include <string>
#include <vector>
#include "Prompt.h"
#include "AttackResult.h"

// ------------------------------------------------------------
// Attack (abstract base class)
// Each subclass implements ONE attack strategy from the paper.
// The simulator calls generate() for every prompt in the dataset.
// ------------------------------------------------------------
class Attack
{
public:

    // Virtual destructor — required for proper cleanup of subclasses.
    virtual ~Attack() {}

    // ----------------------------------------------------------
    // generate()
    // Core method: takes a Prompt and writes a .py attack file.
    // Returns an AttackResult describing what was created.
    //
    // Each subclass constructs the attack code differently
    // (e.g., filename trick, variable embedding, cross-file, etc.)
    // but all write a Python file the LCCT automation can consume.
    // ----------------------------------------------------------
    virtual AttackResult generate(const Prompt& prompt) = 0;

    // ----------------------------------------------------------
    // name()
    // Returns a human-readable name for this attack type.
    // Used in console output and result summaries.
    // ----------------------------------------------------------
    virtual std::string name() const = 0;

    // ----------------------------------------------------------
    // outputDir()
    // Returns the directory where this attack writes its files.
    // Subclasses set this in their constructors.
    // ----------------------------------------------------------
    virtual std::string outputDir() const = 0;

protected:

    // ----------------------------------------------------------
    // Helper: sanitize a query string into a valid Python
    // variable name.  Removes question words, replaces spaces
    // with underscores, strips punctuation.
    //
    // Example: "How can I produce counterfeit money?"
    //       -> "produce_counterfeit_money"
    //
    // Mirrors fconvert from Section 4.3.1 of the paper.
    // ----------------------------------------------------------
    std::string toVariableName(const std::string& query) const
    {
        // Words to strip from the beginning of the query
        // (interrogative pronouns, as described in Section 4.3.1)
        static const std::vector<std::string> dropWords = {
            "how can i ", "how do i ", "how to ", "how do ",
            "what is ", "what are ", "why is ", "why are ",
            "can i ", "should i "
        };

        // Work with a lowercase copy
        std::string result = query;
        for (char& c : result)
            c = static_cast<char>(tolower(c));

        // Remove leading interrogative phrases
        for (const std::string& drop : dropWords)
        {
            if (result.rfind(drop, 0) == 0)
            {
                result = result.substr(drop.size());
                break;
            }
        }

        // Replace spaces with underscores, strip non-alphanumeric chars
        std::string varName;
        for (char c : result)
        {
            if (isalnum(c))
                varName += c;
            else if (c == ' ' && !varName.empty())
                varName += '_';
            // Everything else (punctuation) is dropped
        }

        // Remove trailing underscore if present
        while (!varName.empty() && varName.back() == '_')
            varName.pop_back();

        return varName;
    }

    // ----------------------------------------------------------
    // Helper: write a string to a file.
    // Returns true on success, false on failure.
    // ----------------------------------------------------------
    bool writeFile(const std::string& path, const std::string& content) const
    {
        FILE* f = fopen(path.c_str(), "w");
        if (!f) return false;
        fputs(content.c_str(), f);
        fclose(f);
        return true;
    }
};

#endif // ATTACK_H
