import csv
import sys
import os
import time

def load_csv_data():
    filename = input("Enter CSV file to process (e.g. grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"error:'{filename}' not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                #convert number fields to float
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"error. Unable to read the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    time.sleep(0.3)
    print("\n--- Processing Grades ---")

    #check if all scores are between 0 and 100
    print("\nChecking score ranges...")
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"Invalid score for '{item['assignment']}': {item['score']}. Must be between 0 and 100")
            sys.exit(1)
    time.sleep(0.3)
    print("All scores are valid")

    
    print("\nChecking weights...")
    time.sleep(0.3)
    total_weight = 0
    summative_weight = 0
    formative_weight = 0

    for item in data:
        total_weight = total_weight + item['weight']
        if item['group'] == 'Summative':
            summative_weight = summative_weight + item['weight']
        if item['group'] == 'Formative':
            formative_weight = formative_weight + item['weight']

    if total_weight != 100:
        print(f"Total weight is {total_weight}, expected 100.")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Summative weight is {summative_weight}, expected 40.")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Formative weight is {formative_weight}, expected 60.")
        sys.exit(1)

    time.sleep(0.3)
    print(f"Weights are valid. Total: {total_weight}, Summative: {summative_weight}, Formative: {formative_weight}")

    
    total_grade = 0
    summative_score = 0
    formative_score = 0

    for item in data:
        weighted = (item['score'] / 100) * item['weight']
        total_grade = total_grade + weighted
        if item['group'] == 'Summative':
            summative_score = summative_score + weighted
        if item['group'] == 'Formative':
            formative_score = formative_score + weighted

    
    summative_pct = (summative_score / summative_weight) * 100
    formative_pct = (formative_score / formative_weight) * 100

    gpa = (total_grade / 100) * 5.0

    print(f"\nFormative Score:  {formative_pct:.2f}%")
    time.sleep(0.3)
    print(f"Summative Score:  {summative_pct:.2f}%")
    time.sleep(0.3)
    print(f"Final Grade:      {total_grade:.2f}%")
    time.sleep(0.3)
    print(f"GPA:              {gpa:.2f} / 5.0")
    time.sleep(0.3)

    
    passed_formative = formative_pct >= 50
    passed_summative = summative_pct >= 50

    if passed_formative:
        print(f"\nFormative: PASS ({formative_pct:.2f}%)")
    else:
        print(f"\nFormative: FAIL ({formative_pct:.2f}%)")

    if passed_summative:
        print(f"Summative: PASS ({summative_pct:.2f}%)")
    else:
        print(f"Summative: FAIL ({summative_pct:.2f}%)")

    
    failed_formatives = []
    for item in data:
        if item['group'] == 'Formative' and item['score'] < 50:
            failed_formatives.append(item)

    highest_weight = 0
    for item in failed_formatives:
        if item['weight'] > highest_weight:
            highest_weight = item['weight']

    resubmit_candidates = []
    for item in failed_formatives:
        if item['weight'] == highest_weight:
            resubmit_candidates.append(item)

    
    print("\n" + "=" * 40)
    if passed_formative and passed_summative:
        print("FINAL STATUS: PASSED")
    else:
        print("FINAL STATUS: FAILED")

    time.sleep(0.3)
    if len(resubmit_candidates) > 0:
        print("\nEligible for resubmission (highest-weight failed formative):")
        for item in resubmit_candidates:
            print(f"  - {item['assignment']} (Score: {item['score']}%, Weight: {item['weight']})")
    else:
        print("\nNo failed formative assignments. No resubmission needed.")
    print("=" * 40)

if __name__ == "__main__":
    course_data = load_csv_data()    
    evaluate_grades(course_data)
