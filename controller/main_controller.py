import os
import subprocess
import sys

def run_scheduler():
    print("\nRunning scheduler.py...\n")

    result = subprocess.run(
        [
            sys.executable,
            "../python_scheduler/scheduler.py",
            "--file",
            "../python_scheduler/sample_processes.csv"
        ]
    )
    if result.returncode == 0:
        print("\nScheduler completed.\n")
    else:
        print("\nScheduler failed.\n")
        sys.exit(1)

def run_gantt():
    print("\nRunning gantt.py...\n")

    result = (subprocess.run
    (
        [
            sys.executable,
            "../python_scheduler/gantt.py",
            "--file",
            "../python_scheduler/sample_processes.csv"
        ]
    ))

    if result.returncode == 0:
        print("\nGantt generation completed.\n")
    else:
        print("\nGantt generation failed.\n")
        sys.exit(1)

def main():
    print("=================================")
    print(" EduOS Python Main Controller")
    print("=================================")

    if not os.path.exists("../python_scheduler/sample_processes.csv"):
        print("Error: sample_processes.csv not found.")
        sys.exit(1)

    run_scheduler()
    run_gantt()

    print("\nAll tasks completed successfully.")
    print("Check Documents/screenshots/")

if __name__ == "__main__":
    main()