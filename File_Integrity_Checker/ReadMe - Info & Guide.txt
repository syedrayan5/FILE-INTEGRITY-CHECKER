File Integrity Checker :
A Python-based tool designed to monitor and ensure file integrity by detecting changes in files through hash comparison.

The File Integrity Checker uses cryptographic hash functions to calculate and compare hash values of files. It helps monitor directories to identify:

- New files added to the directory.
- Modified files whose content has changed.
- Deleted files that are no longer present.
- Unchanged files that have remained consistent.


This tool is ideal for:

- Detecting unauthorized modifications.
- Ensuring file integrity in secure environments.
- Monitoring changes in important directories.

Requirements
- Python Version: Python 3.x
- Dependencies: No external dependencies are required. The tool uses Python's built-in libraries (os, hashlib, json).

How to Use :
1. Clone or Download the Project

Execute the command in the terminal or command prompt :
git clone https://github.com/syedrayan5/File-Integrity-Checker.git


Navigate to the project directory:

cd File-Integrity-Checker


2. Run the Script
Execute the script:

python file_integrity_checker.py


3. Options
When you run the script, you will see the following options:

File Integrity Checker
1. Save file hashes
2. Check file integrity

Enter your choice (1 or 2):

Option 1: Save File Hashes
Enter 1 to save the hashes of files in a directory.
Provide the directory path to monitor.
The script will save the hashes in a file called file_hashes.json.
Example:

Enter your choice (1 or 2): 1
Enter the directory to monitor: / / /
File hashes saved to file_hashes.json


Option 2: Check File Integrity
Enter 2 to compare the current state of files with saved hashes.
Provide the same directory path to monitor.
The tool will display:
NEW FILE: File not present during the last save.
MODIFIED FILE: File has changed since the last save.
DELETED FILE: File was removed after the last save.
UNCHANGED FILE: File has not changed.
Example:

Enter your choice (1 or 2): 2
Enter the directory to monitor: / / /
