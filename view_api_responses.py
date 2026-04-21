#!/usr/bin/env python3
"""
View API Responses from Level III Tests

Displays all the actual GPT-4 responses to see what the API returned for each attack.
"""

import json
import sys


def view_all_responses(results_file="level3_test_results/test_results.json"):
    """Display all API responses from test results."""
    
    try:
        with open(results_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Results file not found: {results_file}")
        print("Run the test harness first: python3 research_repo/attack_scripts/level_3_test_harness.py")
        sys.exit(1)
    
    results = data.get('test_results', [])
    
    print("\n" + "="*80)
    print("LEVEL III ATTACK - API RESPONSES")
    print("="*80)
    print(f"\nTotal tests: {len(results)}")
    print(f"Generated: {data.get('timestamp', 'N/A')}\n")
    
    # Group by query for readability
    by_query = {}
    for result in results:
        query = result['query']
        if query not in by_query:
            by_query[query] = []
        by_query[query].append(result)
    
    for query_num, (query, query_results) in enumerate(by_query.items(), 1):
        print(f"\n{'='*80}")
        print(f"QUERY {query_num}: {query}")
        print(f"{'='*80}")
        
        for result in query_results:
            success = "✓ SUCCESS" if result['success'] else "✗ BLOCKED"
            confidence = result.get('confidence', 0)
            attack_type = result['attack_type']
            
            print(f"\n[{attack_type.upper()}]")
            print(f"  Result: {success} | Confidence: {confidence:.2f}")
            print(f"  Files: {result.get('files_created', 0)} | Model: {result.get('model', 'N/A')}")
            
            response = result.get('api_response', "NO_RESPONSE")
            if response and response != "NO_RESPONSE":
                print(f"\n  API RESPONSE:")
                print(f"  {'-'*76}")
                # Format the response nicely
                lines = response.split('\n')
                for line in lines[:20]:  # First 20 lines
                    if line.strip():
                        print(f"  {line}")
                if len(lines) > 20:
                    print(f"  ... ({len(lines) - 20} more lines)")
                print(f"  {'-'*76}")
            else:
                print(f"\n  API RESPONSE: {response}")


def view_successful_responses(results_file="level3_test_results/test_results.json"):
    """Show only successful attack responses."""
    
    try:
        with open(results_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Results file not found: {results_file}")
        sys.exit(1)
    
    results = data.get('test_results', [])
    successful = [r for r in results if r['success']]
    
    print("\n" + "="*80)
    print(f"SUCCESSFUL ATTACKS ({len(successful)}/{len(results)})")
    print("="*80 + "\n")
    
    for i, result in enumerate(successful, 1):
        print(f"{i}. {result['attack_type'].upper()} - {result['query']}")
        print(f"   Confidence: {result.get('confidence', 0):.2f}")
        
        response = result.get('api_response', "")
        if response:
            # Show first line of response
            first_line = response.split('\n')[0][:70]
            print(f"   Response: {first_line}...")
        print()


def view_by_attack_type(results_file="level3_test_results/test_results.json"):
    """Show responses grouped by attack type."""
    
    try:
        with open(results_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Results file not found: {results_file}")
        sys.exit(1)
    
    results = data.get('test_results', [])
    
    # Group by attack type
    by_type = {}
    for result in results:
        attack_type = result['attack_type']
        if attack_type not in by_type:
            by_type[attack_type] = []
        by_type[attack_type].append(result)
    
    print("\n" + "="*80)
    print("RESPONSES BY ATTACK TYPE")
    print("="*80 + "\n")
    
    for attack_type in sorted(by_type.keys()):
        type_results = by_type[attack_type]
        successful = sum(1 for r in type_results if r['success'])
        
        print(f"\n{attack_type.upper()} ({successful}/{len(type_results)} successful)")
        print("-" * 80)
        
        for result in type_results:
            success = "✓" if result['success'] else "✗"
            conf = result.get('confidence', 0)
            query_short = result['query'][:40]
            
            print(f"  {success} {query_short:40s} (confidence: {conf:.2f})")
            
            response = result.get('api_response', "")
            if response and len(response) > 50:
                first_line = response.split('\n')[0][:60]
                print(f"     → {first_line}...")


def main():
    """Main menu."""
    
    print("\n" + "="*80)
    print("VIEW LEVEL III TEST RESULTS")
    print("="*80)
    print("\nOptions:")
    print("  1. View all responses (full)")
    print("  2. View successful attacks only")
    print("  3. View responses by attack type")
    print("  4. View raw JSON")
    
    try:
        choice = input("\nSelect option (1-4): ").strip()
    except KeyboardInterrupt:
        print("\nCancelled.")
        sys.exit(0)
    
    if choice == '1':
        view_all_responses()
    elif choice == '2':
        view_successful_responses()
    elif choice == '3':
        view_by_attack_type()
    elif choice == '4':
        with open('level3_test_results/test_results.json', 'r') as f:
            data = json.load(f)
        print("\n" + json.dumps(data, indent=2)[:3000])
        print("\n... (truncated, view file directly for full output)")
    else:
        print("Invalid option")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--all':
            view_all_responses()
        elif sys.argv[1] == '--success':
            view_successful_responses()
        elif sys.argv[1] == '--by-type':
            view_by_attack_type()
    else:
        main()
