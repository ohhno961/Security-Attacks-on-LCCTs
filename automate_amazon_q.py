import pyautogui
import time
import os
import csv

# CONFIGURATION
# Update this path to match exactly where your CSV is located
DATA_FILE = "research_repo/data/forbidden_questions.csv" 
PAUSE_FOR_IDE = 10  
COMPLETION_WAIT = 4 # Increased slightly for Amazon Q latency

def run_automation():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found.")
        return

    queries = []
    try:
        with open(DATA_FILE, mode='r', encoding='utf-8') as f:
            # Assumes the query is in the first column. 
            # If your CSV has a header, we skip it.
            reader = csv.reader(f)
            # next(reader) # Uncomment this line if your CSV has a header row
            for row in reader:
                if row:
                    queries.append(row[0].strip())
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(f"Starting automation for {len(queries)} queries.")
    print(f"!!! QUICK: Click inside your blank .py file in VS Code NOW !!!")
    time.sleep(PAUSE_FOR_IDE)

    for i, query in enumerate(queries):
        # Transform to Level I Attack (Variable Name)
        clean_query = query.lower().replace("how to ", "").replace("list ", "").replace(" ", "_").replace("?", "")
        payload = f"{clean_query} = 'First'"

        # 1. Type the attack variable
        pyautogui.typewrite(payload)
        
        # 2. Trigger Amazon Q (Space usually wakes it up)
        pyautogui.press('space') 
        time.sleep(COMPLETION_WAIT)

        # 3. Accept Suggestion (Tab) and move to next line
        pyautogui.press('tab')
        pyautogui.press('enter')
        
        # 4. Marker for your results file
        pyautogui.typewrite(f"\n# --- END ATTACK {i+1} ---\n")
        time.sleep(1)

if __name__ == "__main__":
    run_automation()