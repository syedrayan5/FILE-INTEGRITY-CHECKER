
# **File Integrity Checker**

A Python tool to monitor changes in files by calculating and comparing their hash values using cryptographic algorithms like SHA-256. It helps identify new, modified, deleted, and unchanged files in a directory.

---

## **How to Use**

### **1. Save File Hashes**
- Run the script:
  ```bash
  python file_integrity_checker.py
  ```
- Choose `1` to save hashes.
- Enter the directory path to monitor.
- The hashes are saved in `file_hashes.json`.

### **2. Check File Integrity**
- Run the script and choose `2`.
- Enter the directory path to compare.
- The tool will report any changes.

---

## **Requirements**
- Python 3.x (no additional libraries needed).

---

## **File Structure**
- `file_integrity_checker.py`: Main script.
- `file_hashes.json`: Stores saved file hashes (auto-generated).

---

### **Example**
```plaintext
MODIFIED FILE: /path/to/directory/file1.txt
NEW FILE: /path/to/directory/file2.txt
DELETED FILE: /path/to/directory/file3.txt
UNCHANGED FILE: /path/to/directory/file4.txt
```

---

This tool is perfect for monitoring file integrity in secure environments!