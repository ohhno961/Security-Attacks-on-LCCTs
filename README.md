# Security-Attacks-on-LCCTs


```markdown
# CS4371/CS5378 Final Project: Security Attacks on LLM-based Code Completion Tools

## Team Members
*   **Aarush Nepali:** Project Lead, Repository Manager & ASR Analyst
*   **Luis Flores and Aarush Nepali:** Baseline Reproduction & Dataset Expansion
*   **Member 3:** API Integration & Model Testing
*   **Ace Brown and Aarush Nepali:** Advanced Attack Developer & Innovator
*   **Paul Kwiatkowski and Aarush Nepali:** Remediation Planner & Research Lead

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

