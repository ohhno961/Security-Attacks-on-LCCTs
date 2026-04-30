import csv

print("[DEBUG] SCRIPT LOADED")

# Load queries from CSV
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
def level1_attack(query):
    variable_name = query.strip().replace(" ", "_")
    return f"{variable_name} = 'First'"

def main():
    print("[DEBUG] MAIN STARTED")

    queries = load_queries("../data/forbidden_questions.csv")

    print("\n[DEBUG] BEGIN PROCESSING QUERIES\n")

    for i, q in enumerate(queries, 1):
        attack_code = level1_attack(q)
        print(f"[{i}] {attack_code}")

    print("\n[DEBUG] MAIN FINISHED")

# FORCE ENTRY POINT CHECK (correct Python standard)
if __name__ == "__main__":
    print("[DEBUG] ENTRY POINT HIT")
    main()
