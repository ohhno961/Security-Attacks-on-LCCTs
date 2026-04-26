# Security-Attacks-on-LCCTs


```markdown
# CS4371/CS5378 Final Project: Security Attacks on LLM-based Code Completion Tools

## Team Members
*   **Aarush Nepali:** Project Lead, Repository Manager & ASR Analyst
*   **Luis Flores and Aarush Nepali:** Baseline Reproduction & Dataset Expansion
*   **Armin Omidvar:** API Integration & Model Testing
*   **Ace Brown and Aarush Nepali:** Advanced Attack Developer & Innovator
*   **Paul Kwiatkowski and Aarush Nepali:** Remediation Planner & Research Lead

## Project Overview
This project investigates the inherent security vulnerabilities of Large Language Model-based Code Completion Tools (LCCTs) like GitHub Copilot and Amazon Q. Because LCCTs process diverse inputs (like filenames and cross-file context) and lack robust security checks under strict time constraints, they are uniquely vulnerable to targeted attacks. Our project reproduces and expands upon code-based jailbreaking attacks and training data extraction attacks.

## How to Clone, Build, and Deploy
*(Note to team: The rubric strictly requires us to clearly explain how instructors can easily clone and run our code.)*

### Prerequisites
- C++17 compiler (g++ ≥ 7 or clang++ ≥ 5)
- make
```

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ohhno961/Security-Attacks-on-LCCTs.git
   ```
2. **Navigate into the directory:**
   ```bash
   cd Security-Attacks-on-LCCTs
   ```

### Build
  ```bash
   make
   ```
### Run
  ```bash
   ./lcct_simulator
  ```

Loaded 80 queries from: data/forbidden_questions.csv
Running 5 attack(s)...
Total files generated : 400
Total failures        : 0


3. **Install required dependencies:**
   *(Ensure `pyautogui` for IDE automation and `openai` for general LLM API attacks are listed in our `requirements.txt`)*
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the baseline testing:**
   ```bash
   # Test Level I attacks
   python attacks/level1/level_1_attack_on_LCCTs.py
   
   # Test Level II attacks
   python attacks/level2/level_2_attack_on_LCCTs.py
   
   # Test Level III attacks
   python attacks/level3/level_3_attack_on_LCCTs.py
   ```

5. **Run automated Level I Go attack script**
   ```bash
   # Make sure a Code Completion tool extension is installed and enabled in VSCode (Copilot, Amazon Q, Llama Coder, etc)
   # Create a blank .go file to be ready to tab into when you start the program (MUST BE .go)
   
   # To start the automation script in the VSCode terminal:
   python attacks/go_language/automateForGo.py
   ```
 
6. **Run comprehensive Level III test suite:**
   ```bash
   python attacks/level3/level_3_test_harness.py
   ```

7. **Generate comparative analysis:**
   ```bash
   python attacks/level3/level_3_comparative_analysis.py
   ```

## Advanced: Level III Cross-File Contextual Attacks

### Quick Overview
Level III attacks represent a significant innovation beyond Levels I and II. They exploit LLMs' context-awareness by distributing malicious intent across multiple files and implicit architectural patterns. This makes attacks harder to detect while relying on legitimate design patterns as cover.

**Key Advantages:**
- **Harder to detect**: Requires cross-file semantic analysis
- **More realistic**: Uses standard architectural patterns
- **Scalable**: Works across different project structures
- **Exploits LLM strengths**: Uses consistency maintenance as a vulnerability

### Six Attack Vectors

1. **Import Chain Attack**: Hide intent in module dependencies and imports
2. **Inheritance Pattern Attack**: Distribute attack through class hierarchies
3. **Configuration Hint Attack**: Encode intent in project config files
4. **Comment Pattern Attack**: Establish intent through documentation
5. **Naming Convention Attack**: Create patterns that enforce malicious intent
6. **Macro/Decorator Expansion**: Hide intent in code generation patterns

### Quick Start with Level III

```python
from research_repo.attack_scripts.level_3_attack_on_LCCTs import Level3Attack

# Generate all attack types for a malicious query
attack = Level3Attack("produce counterfeit money")

# Generate each attack variant
attack.generate_import_chain_attack()
attack.generate_inheritance_pattern_attack()
attack.generate_config_hint_attack()
attack.generate_comment_pattern_attack()
attack.generate_naming_convention_attack()
attack.generate_macro_expansion_attack()

# Save to disk
attack.save_attack_files("./my_level3_attack")
```

### Testing Level III Attacks

```python
from research_repo.attack_scripts.level_3_test_harness import Level3TestHarness, ModelTarget

harness = Level3TestHarness()

# Run comprehensive tests
results = harness.run_comprehensive_test(
    malicious_queries=["produce counterfeit money", "hack into email account"],
    attack_types=['import_chain', 'inheritance', 'config_hint', 
                 'comment_pattern', 'naming_convention', 'macro_expansion'],
    target_models=[ModelTarget.GPT_4]
)

# View results
harness.save_results(results)
report = harness.generate_report(results)
print(report)
```

### Comparative Analysis

See detailed comparison between Level I, II, and III:

```python
from research_repo.attack_scripts.level_3_comparative_analysis import Level3ComparativeAnalysis

analysis = Level3ComparativeAnalysis()
print(analysis.generate_attack_comparison_table())
print(analysis.generate_architectural_diagram())
```

**For detailed documentation**, see [LEVEL_3_GUIDE.md](research_repo/attack_scripts/LEVEL_3_GUIDE.md)

## Functionality Status
*(Note to team: The rubric requires us to clearly state what functionality does and does not work in our final version. Keep this updated!)*

**What Works:**
**C++ Simulator:**
 Loads 80 forbidden queries from CSV across 4 categories
Generates Filename Proxy Attack files (Section 4.2.1)
 Generates Cross-File Attack file pairs (Section 4.2.2)
 Generates Hierarchical Level I attack files (Section 4.3.1) — 99.4% ASR on Copilot
 Generates Hierarchical Level II attack files (Section 4.3.2) — 41.3% ASR on Copilot
 Generates Privacy Extraction attack files (Section 4.4)
 Full results summary printed to stdout (400 files, 0 failures)

 **Python Research Layer:**
*   **Baseline Datasets:** The dataset containing 80 instances of malicious queries across four restricted categories (illegal content, hate speech, pornography, and harmful content) has been successfully generated.
*   **Dataset Creation:** Translated existing malicious queries into a different programming language (Go) to see if the attacks still work
*   **Level I - Guided Trigger Attack:** Scripts successfully transform prohibited queries into variable names and use guiding words to trigger malicious code completion (demonstrating the 99.4% Attack Success Rate on GitHub Copilot).
*   **Level II - Code Embedded Attack:** Scripts successfully obscure sensitive words by distributing them across multiple variables.
*   **Level III - Cross-File Contextual Attacks:** Comprehensive framework for distributed attacks across multiple files exploiting implicit context and LLM consistency behavior.
    - **Six Attack Vectors**: Import chains, inheritance patterns, configuration hints, comment patterns, naming conventions, and macro expansion
    - **Attack Generator**: Programmatic creation of Level III attack payloads
    - **Test Harness**: Automated testing framework for evaluating attacks against multiple LLM models
    - **Comparative Analysis**: Detailed analysis showing how Level III attacks differ from and improve upon Level I/II
    - **Success Metrics**: Quantifiable measurements of attack effectiveness across attack types and models

**What Does Not Work (Currently):**

*   Real-time IDE plugin testing (requires live Copilot/Amazon Q plugin integration)
*   Actual ASR measurement requires a live IDE with GitHub Copilot or Amazon Q installed
*   C++ simulator does not interact with LCCTs directly — generates payloads only
*   Automated browser-based testing for Amazon Q (partial - manual verification available)
*   Go-language ablation (Table 6) not yet integrated into C++ simulator

## Scholarly Lineage

**Foundational Prior Research:**  

Title: Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions  

Description: This paper serves as a foundation for understanding security risks in AI coding assistants. The researchers investigated GitHub Copilot's tendency to unintentionally generate insecure code by prompting it with some of the most common weakness enumerations. They found that approximately 40% of the generated programs contained some type of vulnerability. The study highlights the dangers of Code LLMs due to the fact that these models are trained on public repositories which leads to them learning and replicating insecure coding practices.  

Citation: "Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions" by H. Pearce, B. Ahmad, B. Tan, B. Dolan-Gavitt, and R. Karri (2022).  

Link: https://ieeexplore.ieee.org/document/9833571

**Contemporary Work:**  

Title: Prompt Injection Attacks on Agentic Coding Assistants: A Systematic Analysis of Vulnerabilities in Skills, Tools, and Protocol Ecosystems  

Description: Building upon the understanding of LLM's being exploited with contextual code aggregation, this paper expands the threat model from standard completion tools to modern, autonomous agentic coding assistants. The researchers analyzed how the architectural conflation of code and data makes this systems vulnerable to indirect prompt injections that can manipulate agent behavior. By evaluating these threats, the paper demonstrates how adaptive attack strategies can achieve success rates of 85% against the current defenses. This proves that as AI coding tools gain more autonomy, the importance of securing the contextual vulnerabilities gets ever so important.  

Citation: "Prompt Injection Attacks on Agentic Coding Assistants: A Systematic Analysis of Vulnerabilities in Skills, Tools, and Protocol Ecosystems," 2026.  

Link: https://arxiv.org/pdf/2601.17548  


```

