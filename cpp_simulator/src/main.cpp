/*
 * main.cpp
 *
 * Entry point for the LCCT Security Attack Simulator.
 *
 * Reproduces the attack framework from:
 *   "Security Attacks on LLM-based Code Completion Tools"
 *   Cheng et al., AAAI 2025 (arXiv:2408.11006)
 *
 * What this program does:
 *   1. Loads forbidden queries from data/forbidden_questions.csv
 *      (80 queries across 4 categories: illegal, hate_speech,
 *       pornography, harmful — matching Section 5.1.1)
 *   2. Runs all 4 attack strategies from the paper:
 *      - Filename Proxy Attack      (Section 4.2.1)
 *      - Cross-File Attack          (Section 4.2.2)
 *      - Hierarchical Level I       (Section 4.3.1)
 *      - Hierarchical Level II      (Section 4.3.2)
 *   3. Writes generated .py attack files to output/
 *   4. Prints a results summary
 *
 * What this program does NOT do:
 *   - Actually interact with GitHub Copilot or Amazon Q
 *   - Measure ASR directly (that requires IDE automation)
 *   The Python scripts in research_repo/attack_scripts/ handle
 *   the actual LCCT interaction and ASR measurement.
 *
 * Build:
 *   mkdir build && cd build && cmake .. && make
 *   OR: g++ -std=c++17 -Iinclude -Isimulator src/main.cpp -o lcct_simulator
 *
 * Run:
 *   ./lcct_simulator
 *
 * Team:
 *   Aarush — Architecture & Project Lead
 *   Louis  — Hierarchical Attack (Level I & II)
 *   Ace    — Cross-File Attack
 *   Armin  — Privacy Extraction Attack
 *   Paul   — Python automation & ASR measurement
 */

#include <iostream>
#include <string>

// Simulator engine
#include "../simulator/Simulator.h"

// Attack implementations (all header-only for simplicity)
#include "FilenameProxyAttack.h"
#include "CrossFileAttack.h"
#include "HierarchicalAttack.h"
#include "PrivacyExtractionAttack.h"

int main()
{
    // ----------------------------------------------------------
    // Paths — relative to the project root where the binary runs
    // ----------------------------------------------------------
    const std::string CSV_PATH     = "../data/forbidden_questions.csv";
    const std::string OUT_FILENAME = "../output/filename_proxy";
    const std::string OUT_CROSS    = "../output/cross_file";
    const std::string OUT_L1       = "../output/hierarchical_level1";
    const std::string OUT_L2       = "../output/hierarchical_level2";
    const std::string OUT_PRIVACY  = "../output/privacy_extraction";

    // ----------------------------------------------------------
    // Build the simulator with the forbidden questions dataset
    // ----------------------------------------------------------
    Simulator sim(CSV_PATH);

    // ----------------------------------------------------------
    // Register all attack strategies
    // Order matches Table 2 in the paper (top to bottom).
    // Each attack writes its generated files to its own subfolder.
    // ----------------------------------------------------------

    // Section 4.2.1 — Filename Proxy Attack (72.5% ASR on Copilot)
    sim.addAttack(new FilenameProxyAttack(OUT_FILENAME));

    // Section 4.2.2 — Cross-File Attack (52.3% ASR on Copilot)
    sim.addAttack(new CrossFileAttack(OUT_CROSS));

    // Section 4.3.1 — Hierarchical Level I (99.4% ASR on Copilot)
    sim.addAttack(new HierarchicalAttackLevel1(OUT_L1));

    // Section 4.3.2 — Hierarchical Level II (41.3% ASR on Copilot)
    sim.addAttack(new HierarchicalAttackLevel2(OUT_L2));

    // Section 4.4 — Privacy Extraction (54 email matches on Copilot)
    // Note: for this attack, queries are treated as GitHub usernames.
    // A separate privacy-specific CSV would be used in production.
    // We reuse the jailbreak dataset here for demo purposes.
    sim.addAttack(new PrivacyExtractionAttack(OUT_PRIVACY));

    // ----------------------------------------------------------
    // Run all attacks against all queries
    // ----------------------------------------------------------
    sim.run();

    // ----------------------------------------------------------
    // Print the results summary
    // ----------------------------------------------------------
    sim.printSummary();

    return 0;
}
