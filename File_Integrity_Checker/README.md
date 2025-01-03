## FILE-INTEGRITY-CHECKER

**COMPANY** : CODTECH IT SOLUTIONS
**NAME** : SYED RAYAN
**INTERN ID** : CT08HWO
**DOMAIN** : CYBERSECURITY AND ETHICAL HACKING
**BATCH DURATION** : December 30th, 2024 to January 30th, 2025
**MENTOR NAME** : NEELA SANTHOSH

# DESCRIPTION OF THE PROJECT

# Name - File Integrity Checker

## Objective
The File Integrity Checker is a Python-based tool designed to monitor and ensure file integrity by detecting changes in files through hash comparison. It helps users identify unauthorized modifications, ensuring the integrity of files in secure environments.

## Key Features
- **Change Detection**: Monitors directories to identify:
  - New files added to the directory.
  - Modified files whose content has changed.
  - Deleted files that are no longer present.
  - Unchanged files that have remained consistent.
- **Hash Comparison**: Utilizes cryptographic hash functions to calculate and compare hash values of files.
- **User -Friendly Interface**: Simple command-line interface for easy interaction with the tool.

## Libraries Used
- **Built-in Libraries**: The tool uses Python's built-in libraries:
  - `os`: For interacting with the operating system and file system.
  - `hashlib`: For generating cryptographic hash values.
  - `json`: For saving and loading file hashes in JSON format.

## Instructions for Usage

- To get started, clone or download the project repository, Navigate to the project directory
- Run the Script
Execute the script using the following command:

python file_integrity_checker.py

- **Options**
When you run the script, you will see the following options:

File Integrity Checker
1. Save file hashes
2. Check file integrity

Enter your choice (1 or 2):

- Option 1: Save File Hashes
 - Enter 1 to save the hashes of files in a directory.
 - Provide the directory path to monitor.
 - The script will save the hashes in a file called file_hashes.json.



- Option 2: Check File Integrity
 - Enter 2 to compare the current state of files with saved hashes.
 - Provide the same directory path to monitor.
 - The tool will display:
NEW FILE: File not present during the last save.
MODIFIED FILE: File has changed since the last save.
DELETED FILE: File was removed after the last save.
UNCHANGED FILE: File has not changed.

## OUTPUT OF THE TASK :
![File Integrity Checker Output](https://github.com/user-attachments/assets/be1fac9c-a0bf-4c55-98bb-95c3293f9f55)


