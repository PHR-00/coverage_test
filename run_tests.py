# import subprocess
# import webbrowser
# import os

# def run_command(command):
#     """Runs a shell command and prints the output."""
#     print(f" Running: {' '.join(command)}")
#     # On Windows, it's often more reliable to run with shell=True
#     result = subprocess.run(command, capture_output=True, text=True, shell=True)
#     if result.stdout:
#         print(result.stdout)
#     if result.stderr:
#         print("Error:")
#         print(result.stderr)
#     return result

# def main():
#     """Main function to execute all steps."""
#     # 1. Use coverage to run PYTEST. This is the key change.
#     # The command `coverage run -m pytest` tells coverage to
#     # use pytest as the test runner.
#     run_command(["coverage", "run", "-m", "pytest"])

#     # 2. Print the coverage report to the console.
#     print("\n" + "="*20 + " COVERAGE CONSOLE REPORT " + "="*20)
#     run_command(["coverage", "report", "-m"])

#     # 3. Generate the HTML report.
#     print("\n" + "="*20 + " GENERATING HTML REPORT " + "="*20)
#     run_command(["coverage", "html"])

#     # 4. Automatically open the HTML report in a browser.
#     report_path = os.path.join("htmlcov", "index.html")
#     if os.path.exists(report_path):
#         print(f"\n HTML report generated at: {report_path}")
#         try:
#             webbrowser.open(f"file://{os.path.realpath(report_path)}")
#         except webbrowser.Error:
#             print("Could not open web browser. Please open the file manually.")
#     else:
#         print("\n Could not generate HTML report because no coverage data was collected.")

# if __name__ == "__main__":
#     main()