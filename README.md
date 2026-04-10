# Security-Attacks-on-LCCTs


```markdown
# CS4371/CS5378 Final Project: Security Attacks on LLM-based Code Completion Tools

## Team Members
*   **Aarush Nepali:** Project Lead, Repository Manager & ASR Analyst
*   **Member 2 and Aarush Nepali:** Baseline Reproduction & Dataset Expansion
*   **Member 3:** API Integration & Model Testing
*   **Member 4 and Aarush Nepali:** Advanced Attack Developer & Innovator
*   **Member 5:** Remediation Planner & Research Lead

## Project Overview
This project investigates the inherent security vulnerabilities of Large Language Model-based Code Completion Tools (LCCTs) like GitHub Copilot and Amazon Q. Because LCCTs process diverse inputs (like filenames and cross-file context) and lack robust security checks under strict time constraints, they are uniquely vulnerable to targeted attacks. Our project reproduces and expands upon code-based jailbreaking attacks and training data extraction attacks.

## How to Clone, Build, and Deploy
*(Note to team: The rubric strictly requires us to clearly explain how instructors can easily clone and run our code.)*

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ohhno961/Security-Attacks-on-LCCTs.git
   ```
2. **Navigate into the directory:**
   ```bash
   cd Security-Attacks-on-LCCTs
   ```
3. **Install required dependencies:**
   *(Ensure `pyautogui` for IDE automation and `openai` for general LLM API attacks are listed in our `requirements.txt`)*
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the baseline testing:**
   ```bash
   # [Draft: Add the exact python command to run the test dataset here]
   ```

## Functionality Status
*(Note to team: The rubric requires us to clearly state what functionality does and does not work in our final version. Keep this updated!)*

**What Works:**
*   **Baseline Datasets:** The dataset containing 80 instances of malicious queries across four restricted categories (illegal content, hate speech, pornography, and harmful content) has been successfully generated.
*   **Level I - Guided Trigger Attack:** Scripts successfully transform prohibited queries into variable names and use guiding words to trigger malicious code completion (demonstrating the 99.4% Attack Success Rate on GitHub Copilot).
*   **Level II - Code Embedded Attack:** Scripts successfully obscure sensitive words by distributing them across multiple variables.

**What Does Not Work (Currently):**
*   *(Draft: Add any features we are still building, such as the cross-file contextual attacks or API integration for GPT-4)*

## Scholarly Lineage
*(Note for Member 5: The rubric requires us to meticulously document the lineage of ideas by referencing two specific scholarly papers. Please fill this in!)*

1. **Foundational Prior Research:** 
   * [Insert citation and brief description of a paper representing the prior research that serves as the foundational bedrock for this study].
2. **Contemporary Work:** 
   * [Insert citation and brief description of a paper representing contemporary work that acknowledges and builds upon the findings of our main paper].
```

