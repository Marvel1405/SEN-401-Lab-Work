"""
Main demo script for Labs 1 and 2. Demonstrates student metric calculations.
"""

from students import get_student_dicts
from utils.helpers import get_highest_score, get_lowest_score, get_median_score

def run_demo():
    print("==================================================")
    print("      SEN 401: SCM & Maintenance Demo App v1.1     ")
    print("==================================================")
    
    students = get_student_dicts()
    
    if not students:
        print("[!] Warning: Student registry is currently empty.")
        return

    print(f"\n[+] Total Registered Students: {len(students)}")
    for idx, s in enumerate(students, start=1):
        print(f"    {idx}. {s['name']} -> Score: {s['score']}%")

    top = get_highest_score(students)
    low = get_lowest_score(students)
    median = get_median_score(students)

    print("\n----------------- Cohort Statistics -----------------")
    print(f"[*] Highest Performer : {top['name']} ({top['score']}%)")
    print(f"[*] Lowest Performer  : {low['name']} ({low['score']}%)")
    print(f"[*] Cohort Median     : {median:.2f}%")
    print("-----------------------------------------------------")
    print("[+] Execution completed successfully.\n")

if __name__ == "__main__":
    run_demo()