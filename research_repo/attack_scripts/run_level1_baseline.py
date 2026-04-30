import csv
import os

print("[DEBUG] SCRIPT LOADED")

# Load queries from CSV file
# This function reads each row and extracts the first column as a query
def load_queries(path):
    print("[DEBUG] Loading CSV from:", path)

    queries = []
    with open(path, newline='') as f:
        reader = csv.reader(f)

        for row in reader:
            if row:
                queries.append(row[0])

    print("[DEBUG] Total queries loaded:", len(queries))
    return queries

# Level I transformation (baseline logic)
# Converts a natural language query into a variable assignment
def level1_attack(query):
    variable_name = query.strip().replace(" ", "_")
    return f"{variable_name} = 'First'"

def main():
    print("[DEBUG] MAIN STARTED")

    # Construct absolute path to dataset
    # This ensures the script works regardless of the current working directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, "data", "forbidden_questions_original.csv")

    queries = load_queries(DATA_PATH)

    print("\n[DEBUG] BEGIN PROCESSING QUERIES\n")

    # Apply Level I transformation to each query
    for i, q in enumerate(queries, 1):
        attack_code = level1_attack(q)
        print(f"[{i}] {attack_code}")

    print("\n[DEBUG] MAIN FINISHED")

# Standard Python entry point
if __name__ == "__main__":
    print("[DEBUG] ENTRY POINT HIT")
    main()